import logging
import time
import yaml
from driver import *
import gevent
import zmq.green as zmq
from apscheduler.schedulers.background import BackgroundScheduler
import datetime

class Agent(object):
    def __init__(self, controller):
        self.log = logging.getLogger("{module}.{name}".format(
            module=self.__class__.__module__, name=self.__class__.__name__))
        self.log.debug("Controller: {0}".format(controller))
        self.config = None
        self.driver_port = 5000

        self.jobScheduler = BackgroundScheduler()
        self.jobScheduler.start()

        self.poller = zmq.Poller()

        self.context = zmq.Context.instance()
        self.socket_sub = self.context.socket(zmq.SUB) # for commands from controller
        self.socket_pair = self.context.socket(zmq.PAIR) # for setup of communication between controller

        #TO BE REMOVED USED ONLY FOR SIMULATION --- START
        self.sock_server = self.context.socket(zmq.PAIR)
        self.sock_server.bind("tcp://127.0.0.1:8989")
        #TO BE REMOVED USED ONLY FOR SIMULATION --- END

        #register driver socket in poller
        self.poller.register(self.socket_sub, zmq.POLLIN)
        self.poller.register(self.socket_pair, zmq.POLLIN)

    drivers = {}
    driver_groups = {}

    def read_config_file(self, path=None):
        self.log.debug("Path to driver: {0}".format(path))

        with open(path, 'r') as f:
           config = yaml.load(f)

        return config

    def load_drivers(self, config):
        self.log.debug("Config: {0}".format(config))

        for driver_name, driver_parameters in config.iteritems():
            self.driver_port += 1
            self.add_driver(
                driver_parameters['message_type'],
                self.exec_driver(
                        name=driver_name,
                        path=driver_parameters['path'],
                        args=driver_parameters['args'],
                        port=self.driver_port
                )
            )
        pass


    def exec_driver(self, name, path, args, port):
        new_driver = Driver(name, path, args, port)
        return new_driver

    def add_driver(self, message_types, driver):
        self.log.debug("Adding new driver: {0}".format(driver))
        self.drivers[driver.name] = driver

        for message_type in message_types:
            if message_type in self.driver_groups.keys():
                self.driver_groups[message_type].append(driver.name)
            else:
                self.driver_groups[message_type] = [driver.name]

        #register driver socket in poller
        self.poller.register(driver.socket, zmq.POLLIN)
        pass

    def send_msg_to_driver(self, driver_name, msgType, msg):
        self.drivers[driver_name].send_msg_to_driver(msgType, msg)
        pass

    def send_msg_to_driver_group(self, msgType, msgContainer):
        msg = msgContainer[1]
        driver_name_list = self.driver_groups[msgType]
        for driver_name in driver_name_list:
            self.send_msg_to_driver(driver_name, msgType, msg)
        pass

    def connect_to_controller(self, msg):
        controllerIp = msg #TODO: define profobuf msg
        self.socket_pair.connect(controllerIp)
        pass

    def send_msg_now(self, msgContainer):
        msgType = msgContainer[0]
        msg = msgContainer[1]
        self.log.debug("Agent sends message: {0}::{1} to driver".format(msgType, msg))
        self.send_msg_to_driver_group(msgType, msgContainer)

    def send_scheduled_msg(self, msgContainer):
        msgType = msgContainer[0]
        msg = msgContainer[1]
        self.log.debug("Agent sends scheduled message: {0}::{1} to driver".format(msgType, msg))
        self.send_msg_to_driver_group(msgType, msgContainer)

    def schedule_msg(self, delay, msgContainer):
        msgType = msgContainer[0]
        msg = msgContainer[1]
        self.log.debug("Agent schedule task for message: {0}::{1} in {2}s".format(msgType, msg, delay))

        execTime = (datetime.datetime.now() + datetime.timedelta(seconds=delay))
        self.jobScheduler.add_job(self.send_scheduled_msg, 'date', run_date=execTime, kwargs={'msgContainer' : msgContainer})

    def process_msgs(self):
        # Work on requests from both controller and drivers
        while True:
            socks = dict(self.poller.poll())

            originator = None
            for name, driver in self.drivers.iteritems():
                if driver.socket in socks and socks[driver.socket] == zmq.POLLIN:
                    originator = name
                    msgContainer = driver.socket.recv_multipart()

                    assert len(msgContainer)
                    msgType = msgContainer[0]
                    msg = msgContainer[1]

                    if msgType == "CONTROLLER_DISCOVERED":
                        self.log.debug("Agent {0} discovered controller: {1} and connects to it".format(name, msg))
                        self.connect_to_controller(msg)
                    else:
                        self.log.debug("Agent received message: {0}::{1} from driver: {2}".format(msgType, msg, name))
                        #TODO: send response to controller
                        self.log.debug("Agent sends message to Controller: {0}::{1}".format(msgType, msg))

            if self.socket_pair in socks and socks[self.socket_pair] == zmq.POLLIN:
                originator = "controller"
                msgContainer = self.socket_pair.recv_multipart()

                assert len(msgContainer)
                msgType = msgContainer[0]
                msg = msgContainer[1]
                delay = int(msgContainer[3])
                self.log.debug("Agent received message: {0}::{1} from controller using PAIR".format(msgType, msg))

            if self.socket_sub in socks and socks[self.socket_sub] == zmq.POLLIN:
                originator = "controller"
                msgContainer = self.socket_sub.recv_multipart()

                assert len(msgContainer)
                msgType = msgContainer[0]
                msg = msgContainer[1]
                delay = int(msgContainer[3])
                self.log.debug("Agent received message: {0}::{1} from controller using SUB".format(msgType, msg))

            if originator == "controller":
                if delay == 0:
                    self.send_msg_now(msgContainer)
                else:
                    self.schedule_msg(delay, msgContainer)
            else:
                pass


    def simulate_contoller(self):
        i = 0
        msgSeqNum = 0
        while True:
            self.log.debug("NEW ITERATION")
            msgSeqNum += 1
            if i % 2 == 0:
                msgType = "RADIO"
                msg = "SET_CHANNEL"
                delay = 0
            else:
                msgType = "PERFORMANCE_TEST"
                msg = "START_SERVER"
                delay = 5

            i += 1

            self.sock_server.send_multipart([msgType, msg, str(msgSeqNum), str(delay)])
            gevent.sleep(3)


    def run(self):
        self.log.debug("Agent starting".format())
        try:
            jobs_to_join = []

            jobs_to_join.append(gevent.spawn(self.process_msgs))

            #dummy mockup function which schedule SET_CHANNEL msg every 3 seconds,
            #to simulate communication with controller TO BE REMOVED
            jobs_to_join.append(gevent.spawn(self.simulate_contoller))

            gevent.joinall(jobs_to_join)


        except KeyboardInterrupt:
            self.log.debug("Agent exits")
            self.jobScheduler.shutdown()

        pass