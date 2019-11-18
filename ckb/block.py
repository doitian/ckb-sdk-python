from typing import Sequence

from . import uncle_block, transaction
from .types import Block, Header, Transaction, UncleBlock, BlockTemplate
from .typing import HexH256, ProposalShortId


def transactions_root(transactions: Sequence[Transaction]) -> HexH256:
    # TODO
    return '0x'


def proposals_hash(proposals: Sequence[ProposalShortId]) -> HexH256:
    # TODO
    return '0x'


def uncles_hash(uncles: Sequence[UncleBlock]) -> HexH256:
    # TODO
    return '0x'


def from_template(template: BlockTemplate) -> Block:
    transactions = [transaction.from_cellbase_template(template['cellbase'])]
    transactions.extend(transaction.from_template(tx) for tx in template['transactions'])

    proposals = template['proposals']

    uncles = list(uncle_block.from_template(uncle) for uncle in template['uncles'])

    header = Header(
        version=template['version'],
        compact_target=template['compact_target'],
        timestamp=template['timestamp'],
        number=template['number'],
        epoch=template['epoch'],
        transactions_root=transactions_root(transactions),
        proposals_hash=proposals_hash(proposals),
        uncles_hash=uncles_hash(uncles),
        parent_hash=template['parent_hash'],
        dao=template['dao']
    )

    return Block(
        header=header,
        uncles=uncles,
        transactions=transactions,
        proposals=proposals
    )
