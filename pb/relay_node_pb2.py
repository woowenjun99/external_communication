# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: relay_node.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10relay_node.proto\x12\nrelay_node\"\x80\x01\n\x06Values\x12\x16\n\x0e\x61\x63\x63\x65leration_x\x18\x01 \x01(\x02\x12\x16\n\x0e\x61\x63\x63\x65leration_y\x18\x02 \x01(\x02\x12\x16\n\x0e\x61\x63\x63\x65leration_z\x18\x03 \x01(\x02\x12\x0e\n\x06gyro_x\x18\x04 \x01(\x02\x12\x0e\n\x06gyro_y\x18\x05 \x01(\x02\x12\x0e\n\x06gyro_z\x18\x06 \x01(\x02\"\x90\x01\n\x14\x46romRelayNodeRequest\x12\x0e\n\x06values\x18\x01 \x03(\x01\x12\x11\n\tplayer_id\x18\x02 \x01(\x05\x12\x16\n\x0eshoot_detected\x18\x03 \x01(\x08\x12\x13\n\x0bir_detected\x18\x04 \x01(\x08\x12\x18\n\x0btest_action\x18\x05 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_test_action\"h\n\x06Player\x12\n\n\x02hp\x18\x01 \x01(\x05\x12\x0f\n\x07\x62ullets\x18\x02 \x01(\x05\x12\r\n\x05\x62ombs\x18\x03 \x01(\x05\x12\x11\n\tshield_hp\x18\x04 \x01(\x05\x12\x0e\n\x06\x64\x65\x61ths\x18\x05 \x01(\x05\x12\x0f\n\x07shields\x18\x06 \x01(\x05\"\x17\n\x15\x46romRelayNodeResponse\"b\n\x10GameStateRequest\x12&\n\nplayer_one\x18\x01 \x01(\x0b\x32\x12.relay_node.Player\x12&\n\nplayer_two\x18\x02 \x01(\x0b\x32\x12.relay_node.Player\"\x13\n\x11GameStateResponse2\xae\x01\n\tRelayNode\x12P\n\tprocessAi\x12 .relay_node.FromRelayNodeRequest\x1a!.relay_node.FromRelayNodeResponse\x12O\n\x10processGameState\x12\x1c.relay_node.GameStateRequest\x1a\x1d.relay_node.GameStateResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'relay_node_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_VALUES']._serialized_start=33
  _globals['_VALUES']._serialized_end=161
  _globals['_FROMRELAYNODEREQUEST']._serialized_start=164
  _globals['_FROMRELAYNODEREQUEST']._serialized_end=308
  _globals['_PLAYER']._serialized_start=310
  _globals['_PLAYER']._serialized_end=414
  _globals['_FROMRELAYNODERESPONSE']._serialized_start=416
  _globals['_FROMRELAYNODERESPONSE']._serialized_end=439
  _globals['_GAMESTATEREQUEST']._serialized_start=441
  _globals['_GAMESTATEREQUEST']._serialized_end=539
  _globals['_GAMESTATERESPONSE']._serialized_start=541
  _globals['_GAMESTATERESPONSE']._serialized_end=560
  _globals['_RELAYNODE']._serialized_start=563
  _globals['_RELAYNODE']._serialized_end=737
# @@protoc_insertion_point(module_scope)
