from typing import Sequence

from .hash import H256_ZEROS, ckb_hasher
from .hex_coder import hex_to_bytes, hex_from_bytes
from .types import HexH256


# Find max pow of two which <= n
def max_pow_of_two(n: int) -> int:
    r = 1
    while n > 0:
        n = n >> 1
        r = r << 1

    return r >> 1


def merge(left: bytes, right: bytes) -> bytes:
    h = ckb_hasher()
    h.update(left)
    h.update(right)
    return h.digest()


def cbmt_root(items: Sequence[HexH256]) -> HexH256:
    items_len = len(items)
    if items_len == 0:
        return H256_ZEROS

    nodes_len = max_pow_of_two(items_len)
    merge_len = items_len - nodes_len
    merge_offset = items_len - merge_len * 2
    nodes = []

    # fill the lowest complete layer
    for i in range(merge_len):
        nodes.append(merge(hex_to_bytes(items[merge_offset + i * 2]), hex_to_bytes(items[merge_offset + i * 2 + 1])))
    for i in range(nodes_len - merge_len):
        nodes.append(hex_to_bytes(items[i]))

    remaining_nodes_len = nodes_len
    while remaining_nodes_len > 1:
        remaining_nodes_len = remaining_nodes_len >> 1
        for i in range(remaining_nodes_len):
            nodes[i] = merge(nodes[i * 2], nodes[i * 2 + 1])

    return HexH256(hex_from_bytes(nodes[0]))
