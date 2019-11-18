import os

import jsonrpcclient

from .typing import BlockNumber, EpochNumber, HexH256
from .types import Header, Block, Transaction, Epoch, BlockReward

DEFAULT_ENDPOINT = os.environ.get('CKB_RPC_URL', 'http://127.0.0.1:8114')


class RPCClient:
    def __init__(self, endpoint: str = DEFAULT_ENDPOINT):
        self.endpoint = endpoint

    def request(self, method: str, *args):
        return jsonrpcclient.request(self.endpoint, method, *args).data.result

    def get_block(self, hash: HexH256) -> Block:
        return self.request('get_block', hash)

    def get_block_by_number(self, number: BlockNumber) -> Block:
        return self.request('get_block_by_number', number)

    def get_header(self, hash: HexH256) -> Header:
        return self.request('get_header', hash)

    def get_header_by_number(self, number: BlockNumber) -> Header:
        return self.request('get_header_by_number', number)

    def get_transaction(self, hash: HexH256) -> Transaction:
        return self.request('get_transaction', hash)

    def get_block_hash(self, number: BlockNumber) -> HexH256:
        return self.request('get_block_hash', number)

    def get_tip_header(self) -> Header:
        return self.request('get_tip_header')

    def get_tip_block_number(self) -> BlockNumber:
        return self.request('get_tip_block_number')

    def get_current_epoch(self) -> Epoch:
        return self.request('get_current_epoch')

    def get_epoch_by_number(self, number: EpochNumber) -> Epoch:
        return self.request('get_epoch_by_number', number)

    def get_cellbase_output_capacity_details(self, hash: HexH256) -> BlockReward:
        return self.request('get_cellbase_output_capacity_details', hash)


rpc = RPCClient()
