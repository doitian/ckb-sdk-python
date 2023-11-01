from .hash import ckb_hash
from .molecule import extend_uint32, extend_uint64, extend_uint128, extend_bytes_array
from .types import Header, HexH256


def extend_serialized_raw_header(buffer: bytearray, header: Header) -> bytearray:
    # struct RawHeader
    # {
    #     version: Uint32,
    #     compact_target: Uint32,
    #     timestamp: Uint64,
    #     number: Uint64,
    #     epoch: Uint64,
    #     parent_hash: Byte32,
    #     transactions_root: Byte32,
    #     proposals_hash: Byte32,
    #     extra_hash: Byte32,
    #     dao: Byte32,
    # }
    extend_uint32(buffer, header['version'])
    extend_uint32(buffer, header['compact_target'])
    extend_uint64(buffer, header['timestamp'])
    extend_uint64(buffer, header['number'])
    extend_uint64(buffer, header['epoch'])
    extend_bytes_array(buffer, header['parent_hash'])
    extend_bytes_array(buffer, header['transactions_root'])
    extend_bytes_array(buffer, header['proposals_hash'])
    extend_bytes_array(buffer, header['extra_hash'])
    extend_bytes_array(buffer, header['dao'])

    return buffer


def extend_serialized_header(buffer: bytearray, header: Header) -> bytearray:
    # struct Header
    # {
    #     raw: RawHeader,
    #     nonce: Uint128,
    # }
    extend_serialized_raw_header(buffer, header)
    extend_uint128(buffer, header['nonce'])

    return buffer


def header_hash(header: Header) -> HexH256:
    buffer = bytearray()
    extend_serialized_header(buffer, header)
    return ckb_hash(buffer)


def pow_hash(header: Header) -> HexH256:
    buffer = bytearray()
    extend_serialized_raw_header(buffer, header)
    return ckb_hash(buffer)
