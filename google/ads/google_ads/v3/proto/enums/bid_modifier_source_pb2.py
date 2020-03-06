# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/enums/bid_modifier_source.proto

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
  name='google/ads/googleads_v3/proto/enums/bid_modifier_source.proto',
  package='google.ads.googleads.v3.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v3.enumsB\026BidModifierSourceProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V3.Enums\312\002\035Google\\Ads\\GoogleAds\\V3\\Enums\352\002!Google::Ads::GoogleAds::V3::Enums'),
  serialized_pb=_b('\n=google/ads/googleads_v3/proto/enums/bid_modifier_source.proto\x12\x1dgoogle.ads.googleads.v3.enums\x1a\x1cgoogle/api/annotations.proto\"f\n\x15\x42idModifierSourceEnum\"M\n\x11\x42idModifierSource\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0c\n\x08\x43\x41MPAIGN\x10\x02\x12\x0c\n\x08\x41\x44_GROUP\x10\x03\x42\xeb\x01\n!com.google.ads.googleads.v3.enumsB\x16\x42idModifierSourceProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V3.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V3\\Enums\xea\x02!Google::Ads::GoogleAds::V3::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_BIDMODIFIERSOURCEENUM_BIDMODIFIERSOURCE = _descriptor.EnumDescriptor(
  name='BidModifierSource',
  full_name='google.ads.googleads.v3.enums.BidModifierSourceEnum.BidModifierSource',
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
      name='CAMPAIGN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AD_GROUP', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=151,
  serialized_end=228,
)
_sym_db.RegisterEnumDescriptor(_BIDMODIFIERSOURCEENUM_BIDMODIFIERSOURCE)


_BIDMODIFIERSOURCEENUM = _descriptor.Descriptor(
  name='BidModifierSourceEnum',
  full_name='google.ads.googleads.v3.enums.BidModifierSourceEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BIDMODIFIERSOURCEENUM_BIDMODIFIERSOURCE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=228,
)

_BIDMODIFIERSOURCEENUM_BIDMODIFIERSOURCE.containing_type = _BIDMODIFIERSOURCEENUM
DESCRIPTOR.message_types_by_name['BidModifierSourceEnum'] = _BIDMODIFIERSOURCEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BidModifierSourceEnum = _reflection.GeneratedProtocolMessageType('BidModifierSourceEnum', (_message.Message,), dict(
  DESCRIPTOR = _BIDMODIFIERSOURCEENUM,
  __module__ = 'google.ads.googleads_v3.proto.enums.bid_modifier_source_pb2'
  ,
  __doc__ = """Container for enum describing possible bid modifier sources.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.enums.BidModifierSourceEnum)
  ))
_sym_db.RegisterMessage(BidModifierSourceEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
