from .hex_coder import hex_to_int, hex_to_bytes
from .types import HexInt, HexBytes


class HeaderBuilder:
    def __init__(self, buffer: bytearray, items_len: int):
        self.buffer = buffer
        self.header_pos = len(buffer)
        self.offset_pos = self.header_pos + 4
        self.body_pos = self.offset_pos + items_len * 4

        if items_len == 0:
            # total bytes
            buffer.extend((4).to_bytes(4, 'little'))
        else:
            # total bytes placeholder
            buffer.extend(b'\0' * 4)
            # first item offset
            buffer.extend((items_len * 4 + 4).to_bytes(4, 'little'))
            self.offset_pos += 4
            # remaining items_len - 1 offsets placeholders
            if items_len > 1:
                buffer.extend(b'\0' * ((items_len - 1) * 4))

    def finish_item(self):
        offset = (len(self.buffer) - self.header_pos).to_bytes(4, 'little')

        if self.offset_pos < self.body_pos:
            self.buffer[self.offset_pos:self.offset_pos + 4] = offset
            self.offset_pos += 4
        else:
            self.buffer[self.header_pos:self.header_pos + 4] = offset


def extend_uint32(buffer: bytearray, n: HexInt):
    buffer.extend(hex_to_int(n).to_bytes(4, 'little'))


def extend_uint64(buffer: bytearray, n: HexInt):
    buffer.extend(hex_to_int(n).to_bytes(8, 'little'))


def extend_uint128(buffer: bytearray, n: HexInt):
    buffer.extend(hex_to_int(n).to_bytes(16, 'little'))


def extend_bytes_array(buffer: bytearray, b: HexBytes):
    buffer.extend(hex_to_bytes(b))


def extend_bytes_fixvec(buffer: bytearray, b: HexBytes):
    binary = hex_to_bytes(b)
    buffer.extend(len(binary).to_bytes(4, 'little'))
    buffer.extend(binary)
