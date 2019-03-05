# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/errors/partial_failure_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/errors/partial_failure_error.proto',
  package='google.ads.googleads.v1.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v1.errorsB\030PartialFailureErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V1.Errors\312\002\036Google\\Ads\\GoogleAds\\V1\\Errors\352\002\"Google::Ads::GoogleAds::V1::Errors'),
  serialized_pb=_b('\n@google/ads/googleads_v1/proto/errors/partial_failure_error.proto\x12\x1egoogle.ads.googleads.v1.errors\x1a\x1cgoogle/api/annotations.proto\"q\n\x17PartialFailureErrorEnum\"V\n\x13PartialFailureError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12!\n\x1dPARTIAL_FAILURE_MODE_REQUIRED\x10\x02\x42\xf3\x01\n\"com.google.ads.googleads.v1.errorsB\x18PartialFailureErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V1.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V1\\Errors\xea\x02\"Google::Ads::GoogleAds::V1::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_PARTIALFAILUREERRORENUM_PARTIALFAILUREERROR = _descriptor.EnumDescriptor(
  name='PartialFailureError',
  full_name='google.ads.googleads.v1.errors.PartialFailureErrorEnum.PartialFailureError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARTIAL_FAILURE_MODE_REQUIRED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=157,
  serialized_end=243,
)
_sym_db.RegisterEnumDescriptor(_PARTIALFAILUREERRORENUM_PARTIALFAILUREERROR)


_PARTIALFAILUREERRORENUM = _descriptor.Descriptor(
  name='PartialFailureErrorEnum',
  full_name='google.ads.googleads.v1.errors.PartialFailureErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PARTIALFAILUREERRORENUM_PARTIALFAILUREERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=243,
)

_PARTIALFAILUREERRORENUM_PARTIALFAILUREERROR.containing_type = _PARTIALFAILUREERRORENUM
DESCRIPTOR.message_types_by_name['PartialFailureErrorEnum'] = _PARTIALFAILUREERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PartialFailureErrorEnum = _reflection.GeneratedProtocolMessageType('PartialFailureErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _PARTIALFAILUREERRORENUM,
  __module__ = 'google.ads.googleads_v1.proto.errors.partial_failure_error_pb2'
  ,
  __doc__ = """Container for enum describing possible partial failure errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.errors.PartialFailureErrorEnum)
  ))
_sym_db.RegisterMessage(PartialFailureErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)