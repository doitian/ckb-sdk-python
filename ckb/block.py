from typing import Sequence

from . import uncle_block, transaction, header, hex_coder
from .cbmt import cbmt_root
from .hash import ckb_hasher, H256_ZEROS
from .transaction import transaction_hash, transaction_witness_hash
from .types import HexBytes, HexH256, ProposalShortId, Block, Header, Transaction, UncleBlock, BlockTemplate


def transactions_root(transactions: Sequence[Transaction]) -> HexH256:
    transaction_hash_root = cbmt_root([transaction_hash(tx) for tx in transactions])
    witness_hash_root = cbmt_root([transaction_witness_hash(tx) for tx in transactions])

    hasher = ckb_hasher()
    hasher.update(hex_coder.hex_to_bytes(transaction_hash_root))
    hasher.update(hex_coder.hex_to_bytes(witness_hash_root))

    return '0x' + hasher.hexdigest()


def proposals_hash(proposals: Sequence[ProposalShortId]) -> HexH256:
    if len(proposals) == 0:
        return H256_ZEROS

    hasher = ckb_hasher()

    for id in proposals:
        hasher.update(hex_coder.hex_to_bytes(id))

    return '0x' + hasher.hexdigest()


def uncles_hash(uncles: Sequence[UncleBlock]) -> HexH256:
    if len(uncles) == 0:
        return H256_ZEROS

    hasher = ckb_hasher()

    for uncle in uncles:
        hasher.update(hex_coder.hex_to_bytes(header.header_hash(uncle['header'])))

    return '0x' + hasher.hexdigest()


def extra_hash(uncles: Sequence[UncleBlock], extension: HexBytes) -> HexH256:
    hash_without_extension = uncles_hash(uncles)
    if extension is not None:
        extension_hasher = ckb_hasher()
        extension_hasher.update(hex_coder.hex_to_bytes(extension))
        extra_hash_digest = hash_without_extension + extension_hasher.hexdigest()
        hasher = ckb_hasher()
        hasher.update(hex_coder.hex_to_bytes(extra_hash_digest))
        return '0x' + hasher.hexdigest()

    return hash_without_extension


def from_template(template: BlockTemplate) -> Block:
    transactions = [transaction.from_cellbase_template(template['cellbase'])]
    transactions.extend(transaction.from_template(tx) for tx in template['transactions'])

    proposals = template['proposals']

    uncles = list(uncle_block.from_template(uncle) for uncle in template['uncles'])

    header = Header(
        version=template['version'],
        compact_target=template['compact_target'],
        timestamp=template['current_time'],
        number=template['number'],
        epoch=template['epoch'],
        transactions_root=transactions_root(transactions),
        proposals_hash=proposals_hash(proposals),
        extra_hash=extra_hash(uncles, template['extension']),
        parent_hash=template['parent_hash'],
        dao=template['dao'],
        nonce='0x0'
    )

    return Block(
        header=header,
        uncles=uncles,
        transactions=transactions,
        proposals=proposals,
        extension=template['extension']
    )
