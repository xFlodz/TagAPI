# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tag.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'tag.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ttag.proto\x12\x03tag\"#\n\x11GetTagByIdRequest\x12\x0e\n\x06tag_id\x18\x01 \x01(\x05\".\n\x12GetTagByIdResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t2O\n\x0egRPCTagService\x12=\n\nGetTagById\x12\x16.tag.GetTagByIdRequest\x1a\x17.tag.GetTagByIdResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tag_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETTAGBYIDREQUEST']._serialized_start=18
  _globals['_GETTAGBYIDREQUEST']._serialized_end=53
  _globals['_GETTAGBYIDRESPONSE']._serialized_start=55
  _globals['_GETTAGBYIDRESPONSE']._serialized_end=101
  _globals['_GRPCTAGSERVICE']._serialized_start=103
  _globals['_GRPCTAGSERVICE']._serialized_end=182
# @@protoc_insertion_point(module_scope)
