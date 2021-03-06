# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mssv.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mssv.proto',
  package='MSSV',
  syntax='proto3',
  serialized_options=b'\n\025io.grpc.examples.MSSVB\tMSSVProtoP\001\242\002\004MSSV',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nmssv.proto\x12\x04MSSV\"\x14\n\x04idSV\x12\x0c\n\x04mssv\x18\x01 \x01(\t\"\x8e\x01\n\x06infoSV\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x02id\x18\x02 \x01(\x0b\x32\n.MSSV.idSV\x12\r\n\x05phone\x18\x03 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x61teOfBirth\x18\x05 \x01(\t\x12\x0b\n\x03\x61ge\x18\x06 \x01(\t\x12\x0e\n\x06gender\x18\x07 \x01(\t\x12\x0c\n\x04mail\x18\x08 \x01(\t25\n\tMSSVProto\x12(\n\nGetFeature\x12\n.MSSV.idSV\x1a\x0c.MSSV.infoSV\"\x00\x42+\n\x15io.grpc.examples.MSSVB\tMSSVProtoP\x01\xa2\x02\x04MSSVb\x06proto3'
)




_IDSV = _descriptor.Descriptor(
  name='idSV',
  full_name='MSSV.idSV',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mssv', full_name='MSSV.idSV.mssv', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=40,
)


_INFOSV = _descriptor.Descriptor(
  name='infoSV',
  full_name='MSSV.infoSV',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='MSSV.infoSV.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='MSSV.infoSV.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone', full_name='MSSV.infoSV.phone', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='MSSV.infoSV.address', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dateOfBirth', full_name='MSSV.infoSV.dateOfBirth', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='age', full_name='MSSV.infoSV.age', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gender', full_name='MSSV.infoSV.gender', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mail', full_name='MSSV.infoSV.mail', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=185,
)

_INFOSV.fields_by_name['id'].message_type = _IDSV
DESCRIPTOR.message_types_by_name['idSV'] = _IDSV
DESCRIPTOR.message_types_by_name['infoSV'] = _INFOSV
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

idSV = _reflection.GeneratedProtocolMessageType('idSV', (_message.Message,), {
  'DESCRIPTOR' : _IDSV,
  '__module__' : 'mssv_pb2'
  # @@protoc_insertion_point(class_scope:MSSV.idSV)
  })
_sym_db.RegisterMessage(idSV)

infoSV = _reflection.GeneratedProtocolMessageType('infoSV', (_message.Message,), {
  'DESCRIPTOR' : _INFOSV,
  '__module__' : 'mssv_pb2'
  # @@protoc_insertion_point(class_scope:MSSV.infoSV)
  })
_sym_db.RegisterMessage(infoSV)


DESCRIPTOR._options = None

_MSSVPROTO = _descriptor.ServiceDescriptor(
  name='MSSVProto',
  full_name='MSSV.MSSVProto',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=187,
  serialized_end=240,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeature',
    full_name='MSSV.MSSVProto.GetFeature',
    index=0,
    containing_service=None,
    input_type=_IDSV,
    output_type=_INFOSV,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSSVPROTO)

DESCRIPTOR.services_by_name['MSSVProto'] = _MSSVPROTO

# @@protoc_insertion_point(module_scope)
