# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/resources/geographic_view.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.enums import geo_targeting_type_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_geo__targeting__type__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/resources/geographic_view.proto',
  package='google.ads.googleads.v3.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v3.resourcesB\023GeographicViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V3.Resources\312\002!Google\\Ads\\GoogleAds\\V3\\Resources\352\002%Google::Ads::GoogleAds::V3::Resources'),
  serialized_pb=_b('\n=google/ads/googleads_v3/proto/resources/geographic_view.proto\x12!google.ads.googleads.v3.resources\x1a<google/ads/googleads_v3/proto/enums/geo_targeting_type.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xa5\x02\n\x0eGeographicView\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12[\n\rlocation_type\x18\x03 \x01(\x0e\x32\x44.google.ads.googleads.v3.enums.GeoTargetingTypeEnum.GeoTargetingType\x12\x39\n\x14\x63ountry_criterion_id\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value:d\xea\x41\x61\n\'googleads.googleapis.com/GeographicView\x12\x36\x63ustomers/{customer}/geographicViews/{geographic_view}B\x80\x02\n%com.google.ads.googleads.v3.resourcesB\x13GeographicViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V3.Resources\xca\x02!Google\\Ads\\GoogleAds\\V3\\Resources\xea\x02%Google::Ads::GoogleAds::V3::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_geo__targeting__type__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GEOGRAPHICVIEW = _descriptor.Descriptor(
  name='GeographicView',
  full_name='google.ads.googleads.v3.resources.GeographicView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.resources.GeographicView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location_type', full_name='google.ads.googleads.v3.resources.GeographicView.location_type', index=1,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country_criterion_id', full_name='google.ads.googleads.v3.resources.GeographicView.country_criterion_id', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\352Aa\n\'googleads.googleapis.com/GeographicView\0226customers/{customer}/geographicViews/{geographic_view}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=545,
)

_GEOGRAPHICVIEW.fields_by_name['location_type'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_geo__targeting__type__pb2._GEOTARGETINGTYPEENUM_GEOTARGETINGTYPE
_GEOGRAPHICVIEW.fields_by_name['country_criterion_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
DESCRIPTOR.message_types_by_name['GeographicView'] = _GEOGRAPHICVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GeographicView = _reflection.GeneratedProtocolMessageType('GeographicView', (_message.Message,), dict(
  DESCRIPTOR = _GEOGRAPHICVIEW,
  __module__ = 'google.ads.googleads_v3.proto.resources.geographic_view_pb2'
  ,
  __doc__ = """A geographic view.
  
  Geographic View includes all metrics aggregated at the country level,
  one row per country. It reports metrics at either actual physical
  location of the user or an area of interest. If other segment fields are
  used, you may get more than one row per country.
  
  
  Attributes:
      resource_name:
          The resource name of the geographic view. Geographic view
          resource names have the form:  ``customers/{customer_id}/geogr
          aphicViews/{country_criterion_id}~{location_type}``
      location_type:
          Type of the geo targeting of the campaign.
      country_criterion_id:
          Criterion Id for the country.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.resources.GeographicView)
  ))
_sym_db.RegisterMessage(GeographicView)


DESCRIPTOR._options = None
_GEOGRAPHICVIEW._options = None
# @@protoc_insertion_point(module_scope)
