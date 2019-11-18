from .types import HexBytes, HexInt


def hex_to_int(i: HexInt) -> int:
    return int(i, 0)


def hex_from_int(i: int) -> HexInt:
    return HexInt(hex(i))


def hex_to_bytes(b: HexBytes) -> bytes:
    return bytes.fromhex(b[2:])


def hex_from_bytes(b: bytes) -> HexBytes:
    return HexBytes('0x' + b.hex())
