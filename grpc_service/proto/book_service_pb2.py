# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: book_service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'book_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x62ook_service.proto\x12\x05\x62ooks\"\x1c\n\x0eGetBookRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x14\n\x12GetAllBooksRequest\"S\n\x0c\x42ookResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x18\n\x10publication_date\x18\x04 \x01(\t\"6\n\x10\x42ookListResponse\x12\"\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\x13.books.BookResponse2\x8b\x01\n\x0b\x42ookService\x12\x39\n\x0bGetBookById\x12\x15.books.GetBookRequest\x1a\x13.books.BookResponse\x12\x41\n\x0bGetAllBooks\x12\x19.books.GetAllBooksRequest\x1a\x17.books.BookListResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'book_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETBOOKREQUEST']._serialized_start=29
  _globals['_GETBOOKREQUEST']._serialized_end=57
  _globals['_GETALLBOOKSREQUEST']._serialized_start=59
  _globals['_GETALLBOOKSREQUEST']._serialized_end=79
  _globals['_BOOKRESPONSE']._serialized_start=81
  _globals['_BOOKRESPONSE']._serialized_end=164
  _globals['_BOOKLISTRESPONSE']._serialized_start=166
  _globals['_BOOKLISTRESPONSE']._serialized_end=220
  _globals['_BOOKSERVICE']._serialized_start=223
  _globals['_BOOKSERVICE']._serialized_end=362
# @@protoc_insertion_point(module_scope)
