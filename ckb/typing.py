from typing_extensions import TypedDict
from typing import NewType, Union

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
