# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='wishful_framework',
  serialized_pb=_b('\n\x0emessages.proto\x12\x11wishful_framework\"\xd2\x01\n\x0eMsgDescription\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\x13\n\x0bsource_uuid\x18\x02 \x02(\t\x12Q\n\x12serialization_type\x18\x03 \x02(\x0e\x32/.wishful_framework.MsgDescription.Serialization:\x04NONE\"J\n\rSerialization\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04JSON\x10\x01\x12\n\n\x06PICKLE\x10\x02\x12\x0b\n\x07MSGPACK\x10\x03\x12\x0c\n\x08PROTOBUF\x10\x04\"\"\n\x06\x44\x65vice\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x02(\t\"\x88\x03\n\x06Module\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x02(\t\x12)\n\x06\x64\x65vice\x18\x03 \x01(\x0b\x32\x19.wishful_framework.Device\x12\x37\n\nattributes\x18\x04 \x03(\x0b\x32#.wishful_framework.Module.Attribute\x12\x35\n\tfunctions\x18\x05 \x03(\x0b\x32\".wishful_framework.Module.Function\x12/\n\x06\x65vents\x18\x06 \x03(\x0b\x32\x1f.wishful_framework.Module.Event\x12\x33\n\x08services\x18\x07 \x03(\x0b\x32!.wishful_framework.Module.Service\x1a\x19\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x02(\t\x1a\x18\n\x08\x46unction\x12\x0c\n\x04name\x18\x01 \x02(\t\x1a\x15\n\x05\x45vent\x12\x0c\n\x04name\x18\x01 \x02(\t\x1a\x17\n\x07Service\x12\x0c\n\x04name\x18\x01 \x02(\t\"u\n\x0bNodeInfoMsg\x12\x12\n\nagent_uuid\x18\x01 \x02(\t\x12\n\n\x02ip\x18\x02 \x02(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04info\x18\x04 \x01(\t\x12*\n\x07modules\x18\x05 \x03(\x0b\x32\x19.wishful_framework.Module\"%\n\x0fNodeInfoRequest\x12\x12\n\nagent_uuid\x18\x01 \x02(\t\")\n\x13NodeAddNotification\x12\x12\n\nagent_uuid\x18\x01 \x02(\t\"Y\n\nNewNodeAck\x12\x0e\n\x06status\x18\x01 \x02(\x08\x12\x17\n\x0f\x63ontroller_uuid\x18\x02 \x01(\t\x12\x12\n\nagent_uuid\x18\x03 \x01(\t\x12\x0e\n\x06topics\x18\x04 \x03(\t\"1\n\x0bNodeExitMsg\x12\x12\n\nagent_uuid\x18\x01 \x02(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\")\n\x08HelloMsg\x12\x0c\n\x04uuid\x18\x01 \x02(\t\x12\x0f\n\x07timeout\x18\x02 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_MSGDESCRIPTION_SERIALIZATION = _descriptor.EnumDescriptor(
  name='Serialization',
  full_name='wishful_framework.MsgDescription.Serialization',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JSON', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PICKLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSGPACK', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTOBUF', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=174,
  serialized_end=248,
)
_sym_db.RegisterEnumDescriptor(_MSGDESCRIPTION_SERIALIZATION)


_MSGDESCRIPTION = _descriptor.Descriptor(
  name='MsgDescription',
  full_name='wishful_framework.MsgDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='wishful_framework.MsgDescription.type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_uuid', full_name='wishful_framework.MsgDescription.source_uuid', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serialization_type', full_name='wishful_framework.MsgDescription.serialization_type', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MSGDESCRIPTION_SERIALIZATION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=248,
)


_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='wishful_framework.Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='wishful_framework.Device.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_framework.Device.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=284,
)


_MODULE_ATTRIBUTE = _descriptor.Descriptor(
  name='Attribute',
  full_name='wishful_framework.Module.Attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_framework.Module.Attribute.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=580,
  serialized_end=605,
)

_MODULE_FUNCTION = _descriptor.Descriptor(
  name='Function',
  full_name='wishful_framework.Module.Function',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_framework.Module.Function.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=607,
  serialized_end=631,
)

_MODULE_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='wishful_framework.Module.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_framework.Module.Event.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=633,
  serialized_end=654,
)

_MODULE_SERVICE = _descriptor.Descriptor(
  name='Service',
  full_name='wishful_framework.Module.Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_framework.Module.Service.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=656,
  serialized_end=679,
)

_MODULE = _descriptor.Descriptor(
  name='Module',
  full_name='wishful_framework.Module',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='wishful_framework.Module.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_framework.Module.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device', full_name='wishful_framework.Module.device', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='wishful_framework.Module.attributes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='functions', full_name='wishful_framework.Module.functions', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='events', full_name='wishful_framework.Module.events', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='services', full_name='wishful_framework.Module.services', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MODULE_ATTRIBUTE, _MODULE_FUNCTION, _MODULE_EVENT, _MODULE_SERVICE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=679,
)


_NODEINFOMSG = _descriptor.Descriptor(
  name='NodeInfoMsg',
  full_name='wishful_framework.NodeInfoMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_uuid', full_name='wishful_framework.NodeInfoMsg.agent_uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip', full_name='wishful_framework.NodeInfoMsg.ip', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_framework.NodeInfoMsg.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='wishful_framework.NodeInfoMsg.info', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modules', full_name='wishful_framework.NodeInfoMsg.modules', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=681,
  serialized_end=798,
)


_NODEINFOREQUEST = _descriptor.Descriptor(
  name='NodeInfoRequest',
  full_name='wishful_framework.NodeInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_uuid', full_name='wishful_framework.NodeInfoRequest.agent_uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=800,
  serialized_end=837,
)


_NODEADDNOTIFICATION = _descriptor.Descriptor(
  name='NodeAddNotification',
  full_name='wishful_framework.NodeAddNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_uuid', full_name='wishful_framework.NodeAddNotification.agent_uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=839,
  serialized_end=880,
)


_NEWNODEACK = _descriptor.Descriptor(
  name='NewNodeAck',
  full_name='wishful_framework.NewNodeAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wishful_framework.NewNodeAck.status', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='controller_uuid', full_name='wishful_framework.NewNodeAck.controller_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='agent_uuid', full_name='wishful_framework.NewNodeAck.agent_uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topics', full_name='wishful_framework.NewNodeAck.topics', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=882,
  serialized_end=971,
)


_NODEEXITMSG = _descriptor.Descriptor(
  name='NodeExitMsg',
  full_name='wishful_framework.NodeExitMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_uuid', full_name='wishful_framework.NodeExitMsg.agent_uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='wishful_framework.NodeExitMsg.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=973,
  serialized_end=1022,
)


_HELLOMSG = _descriptor.Descriptor(
  name='HelloMsg',
  full_name='wishful_framework.HelloMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='wishful_framework.HelloMsg.uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='wishful_framework.HelloMsg.timeout', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1024,
  serialized_end=1065,
)

_MSGDESCRIPTION.fields_by_name['serialization_type'].enum_type = _MSGDESCRIPTION_SERIALIZATION
_MSGDESCRIPTION_SERIALIZATION.containing_type = _MSGDESCRIPTION
_MODULE_ATTRIBUTE.containing_type = _MODULE
_MODULE_FUNCTION.containing_type = _MODULE
_MODULE_EVENT.containing_type = _MODULE
_MODULE_SERVICE.containing_type = _MODULE
_MODULE.fields_by_name['device'].message_type = _DEVICE
_MODULE.fields_by_name['attributes'].message_type = _MODULE_ATTRIBUTE
_MODULE.fields_by_name['functions'].message_type = _MODULE_FUNCTION
_MODULE.fields_by_name['events'].message_type = _MODULE_EVENT
_MODULE.fields_by_name['services'].message_type = _MODULE_SERVICE
_NODEINFOMSG.fields_by_name['modules'].message_type = _MODULE
DESCRIPTOR.message_types_by_name['MsgDescription'] = _MSGDESCRIPTION
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['Module'] = _MODULE
DESCRIPTOR.message_types_by_name['NodeInfoMsg'] = _NODEINFOMSG
DESCRIPTOR.message_types_by_name['NodeInfoRequest'] = _NODEINFOREQUEST
DESCRIPTOR.message_types_by_name['NodeAddNotification'] = _NODEADDNOTIFICATION
DESCRIPTOR.message_types_by_name['NewNodeAck'] = _NEWNODEACK
DESCRIPTOR.message_types_by_name['NodeExitMsg'] = _NODEEXITMSG
DESCRIPTOR.message_types_by_name['HelloMsg'] = _HELLOMSG

MsgDescription = _reflection.GeneratedProtocolMessageType('MsgDescription', (_message.Message,), dict(
  DESCRIPTOR = _MSGDESCRIPTION,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:wishful_framework.MsgDescription)
  ))
_sym_db.RegisterMessage(MsgDescription)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), dict(
  DESCRIPTOR = _DEVICE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:wishful_framework.Device)
  ))
_sym_db.RegisterMessage(Device)

Module = _reflection.GeneratedProtocolMessageType('Module', (_message.Message,), dict(

  Attribute = _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), dict(
    DESCRIPTOR = _MODULE_ATTRIBUTE,
    __module__ = 'messages_pb2'
    # @@protoc_insertion_point(class_scope:wishful_framework.Module.Attribute)
    ))
  ,

  Function = _reflection.GeneratedProtocolMessageType('Function', (_message.Message,), dict(
    DESCRIPTOR = _MODULE_FUNCTION,
    __module__ = 'messages_pb2'
    # @@protoc_insertion_point(class_scope:wishful_framework.Module.Function)
    ))
  ,

  Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
    DESCRIPTOR = _MODULE_EVENT,
    __module__ = 'messages_pb2'
    # @@protoc_insertion_point(class_scope:wishful_framework.Module.Event)
    ))
  ,

  Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), dict(
    DESCRIPTOR = _MODULE_SERVICE,
    __module__ = 'messages_pb2'
    # @@protoc_insertion_point(class_scope:wishful_framework.Module.Service)
    ))
  ,
  DESCRIPTOR = _MODULE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:wishful_framework.Module)
  ))
_sym_db.RegisterMessage(Module)
_sym_db.RegisterMessage(Module.Attribute)
_sym_db.RegisterMessage(Module.Function)
_sym_db.RegisterMessage(Module.Event)
_sym_db.RegisterMessage(Module.Service)

NodeInfoMsg = _reflection.GeneratedProtocolMessageType('NodeInfoMsg', (_message.Message,), dict(
  DESCRIPTOR = _NODEINFOMSG,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:wishful_framework.NodeInfoMsg)
  ))
_sym_db.RegisterMessage(NodeInfoMsg)

NodeInfoRequest = _reflection.GeneratedProtocolMessageType('NodeInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _NODEINFOREQUEST,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:wishful_framework.NodeInfoRequest)
  ))
_sym_db.RegisterMessage(NodeInfoRequest)

NodeAddNotification = _reflection.GeneratedProtocolMessageType('NodeAddNotification', (_message.Message,), dict(
  DESCRIPTOR = _NODEADDNOTIFICATION,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:wishful_framework.NodeAddNotification)
  ))
_sym_db.RegisterMessage(NodeAddNotification)

NewNodeAck = _reflection.GeneratedProtocolMessageType('NewNodeAck', (_message.Message,), dict(
  DESCRIPTOR = _NEWNODEACK,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:wishful_framework.NewNodeAck)
  ))
_sym_db.RegisterMessage(NewNodeAck)

NodeExitMsg = _reflection.GeneratedProtocolMessageType('NodeExitMsg', (_message.Message,), dict(
  DESCRIPTOR = _NODEEXITMSG,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:wishful_framework.NodeExitMsg)
  ))
_sym_db.RegisterMessage(NodeExitMsg)

HelloMsg = _reflection.GeneratedProtocolMessageType('HelloMsg', (_message.Message,), dict(
  DESCRIPTOR = _HELLOMSG,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:wishful_framework.HelloMsg)
  ))
_sym_db.RegisterMessage(HelloMsg)


# @@protoc_insertion_point(module_scope)
