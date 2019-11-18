import hashlib

from .types import HexH256

H256_ZEROS: HexH256 = '0x0000000000000000000000000000000000000000000000000000000000000000'


def ckb_hasher():
    return hashlib.blake2b(digest_size=32, person=b'ckb-default-hash')


def ckb_hash(message: bytes) -> HexH256:
    hasher = ckb_hasher()
    hasher.update(message)
    return '0x' + hasher.hexdigest()
