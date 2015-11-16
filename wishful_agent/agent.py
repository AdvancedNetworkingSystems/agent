import logging
import time
import yaml
from driver import *
import gevent
import zmq.green as zmq

class Agent(object):
    def __init__(self, controller):
        self.log = logging.getLogger("{module}.{name}".format(
            module=self.__class__.__module__, name=self.__class__.__name__))
        self.log.debug("Controller: {0}".format(controller))
        self.config = None
        self.driver_port = 5000

        self.poller = zmq.Poller()

        self.context = zmq.Context.instance()
        self.socket_sub = self.context.socket(zmq.SUB) # for commands from controller
        self.socket_pair = self.context.socket(zmq.PAIR) # for setup of communication between controller

        #TO BE REMOVED USED ONLY FOR SIMULATION --- START
        self.sock_server = self.context.socket(zmq.PAIR)
        self.sock_server.bind("tcp://127.0.0.1:8989")
        self.socket_pair.connect("tcp://127.0.0.1:8989")
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

    def send_msg_to_driver(self, driver_name, msg):
        self.drivers[driver_name].send_msg_to_driver(msg)
        pass

    def send_msg_to_driver_group(self, message_type_name, msg):
        driver_name_list = self.driver_groups[message_type_name]
        for driver_name in driver_name_list:
            self.send_msg_to_driver(driver_name, msg)
        pass

    def process_msgs(self):
        # Work on requests from both controller and drivers
        while True:
            socks = dict(self.poller.poll())

            originator = None
            for name, driver in self.drivers.iteritems():
                if driver.socket in socks and socks[driver.socket] == zmq.POLLIN:
                    originator = name
                    msg = driver.socket.recv()
                    self.log.debug("Agent received message: {0} from driver: {1}".format(msg, name))
                    #TODO: send response to controller
                    self.log.debug("Agent sends message to Controller: {0}".format(msg))

            if self.socket_pair in socks and socks[self.socket_pair] == zmq.POLLIN:
                originator = "contoller"
                msg = self.socket_pair.recv()
                self.log.debug("Agent received message: {0} from controller using PAIR".format(msg))

            if self.socket_sub in socks and socks[self.socket_sub] == zmq.POLLIN:
                originator = "contoller"
                msg = self.socket_sub.recv()
                self.log.debug("Agent received message: {0} from controller using SUB".format(msg))

            #TODO: get msg type
            msgType = msg;
            if originator == "contoller":
                self.log.debug("Agent sends message: {0} to driver".format(msg))
                if msgType == "SET_CHANNEL":
                    #self.send_msg_to_driver("ath9k_driver", "msg for ath9k_driver : SET CHANNEL")
                    #self.send_msg_to_driver_group("radio", "msg for radio drivers : SET CHANNEL")
                    self.send_msg_to_driver_group("wifi", msg)
                elif msgType == "START_SERVER":
                    #self.send_msg_to_driver("iperf_driver", "msg for iperf_driver : START IPERF")
                    self.send_msg_to_driver_group("performance_test", msg)
                else:
                    self.log.debug("Message Type {0} not supported".format(msgType))
                    #self.send_msg_to_driver_group("all", "msg for all drivers")
            else:
                pass


    def simulate_contoller(self):
        while True:
            self.log.debug("NEW ITERATION")
            msg = "SET_CHANNEL"
            self.sock_server.send(msg)
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

        pass