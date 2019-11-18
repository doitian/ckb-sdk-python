from .typing import TypedDict, HexBytes, HexByte32, HexH256, HexInt, BlockNumber, EpochNumber, EpochNumberWithFraction, ProposalShortId, DepType, ScriptHashType
from typing import Optional, Sequence

Header = TypedDict('Header', {
    'version': HexInt,
    'compact_target': HexInt,
    'timestamp': HexInt,
    'number': BlockNumber,
    'epoch': EpochNumberWithFraction,
    'parent_hash': HexH256,
    'transactions_root': HexH256,
    'proposals_hash': HexH256,
    'uncles_hash': HexH256,
    'dao': HexByte32,
    'nonce': HexInt,
    'hash': Optional[HexH256]
})

UncleBlock = TypedDict('UncleBlock', {
    'header': Header,
    'proposals': Sequence[ProposalShortId]
})

OutPoint = TypedDict('OutPoint', {
    'tx_hash': HexH256,
    'index': HexInt
})

CellDep = TypedDict('CellDep', {
    'out_point': OutPoint,
    'dep_type': DepType
})

CellInput = TypedDict('CellInput', {
    'since': HexInt,
    'previous_output': OutPoint
})

Script = TypedDict('Script', {
    'code_hash': HexH256,
    'hash_type': ScriptHashType,
    'args': HexBytes
})

CellOutput = TypedDict('CellOutput', {
    'capacity': HexInt,
    'lock': Script,
    'type': Optional[Script]
})

Transaction = TypedDict('Transaction', {
    'version': HexInt,
    'cell_deps': Sequence[CellDep],
    'header_deps': Sequence[HexH256],
    'inputs': Sequence[CellInput],
    'outputs': Sequence[CellOutput],
    'outputs_data': Sequence[HexBytes],
    'witnesses': Sequence[HexBytes],
    'hash': Optional[HexH256]
})

Block = TypedDict('Block', {
    'header': Header,
    'uncles': Sequence[UncleBlock],
    'transactions': Sequence[Transaction],
    'proposals': Sequence[ProposalShortId]
})

Epoch = TypedDict('Epoch', {
    'number': EpochNumber,
    'start_number': BlockNumber,
    'length': BlockNumber,
    'compact_target': HexInt
})

BlockReward = TypedDict('BlockReward', {
    'total': HexInt,
    'primary': HexInt,
    'secondary': HexInt,
    'tx_fee': HexInt,
    'proposal_reward': HexInt
})
