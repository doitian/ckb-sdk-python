from typing import Optional, Sequence, NewType, Union

from typing_extensions import TypedDict

HexBytes = NewType('HexBytes', str)
HexByte32 = NewType('HexByte32', HexBytes)
HexH256 = NewType('HexH256', HexBytes)
HexInt = NewType('HexInt', str)

BlockNumber = NewType('BlockNumber', HexInt)
EpochNumber = NewType('EpochNumber', HexInt)
EpochNumberWithFraction = NewType('EpochNumberWithFraction', HexInt)
ProposalShortId = NewType('ProposalShortId', HexBytes)

DepType = Union['code', 'dep_group']
ScriptHashType = Union['data', 'type']

Header = TypedDict('Header', {
    'version': HexInt,
    'compact_target': HexInt,
    'timestamp': HexInt,
    'number': BlockNumber,
    'epoch': EpochNumberWithFraction,
    'parent_hash': HexH256,
    'transactions_root': HexH256,
    'proposals_hash': HexH256,
    'extra_hash': HexH256,
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
    'proposals': Sequence[ProposalShortId],
    'extension': HexBytes
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

UncleTemplate = TypedDict('UncleTemplate', {
    'hash': HexH256,
    'required': bool,
    'proposals': Sequence[ProposalShortId],
    'header': Header
})

TransactionTemplate = TypedDict('TransactionTemplate', {
    'hash': HexH256,
    'required': bool,
    'cycles': Optional[HexInt],
    'depends': Optional[Sequence[HexInt]],
    'data': Transaction
})

CellbaseTemplate = TypedDict('CellbaseTemplate', {
    'hash': HexH256,
    'cycles': Optional[HexInt],
    'data': Transaction
})

BlockTemplate = TypedDict('BlockTemplate', {
    'version': HexInt,
    'compact_target': HexInt,
    'current_time': HexInt,
    'number': BlockNumber,
    'epoch': EpochNumberWithFraction,
    'parent_hash': HexH256,
    'cycles_limit': HexInt,
    'bytes_limit': HexInt,
    'uncles_count_limit': HexInt,
    'uncles': Sequence[UncleTemplate],
    'transactions': Sequence[TransactionTemplate],
    'proposals': Sequence[ProposalShortId],
    'cellbase': CellbaseTemplate,
    'work_id': HexInt,
    'dao': HexByte32,
    'extension': HexBytes
})
