import os

import jsonrpcclient

DEFAULT_ENDPOINT = os.environ.get('CKB_RPC_URL', 'http://127.0.0.1:8114')


class RPCClient:
    def __init__(self, endpoint: str = DEFAULT_ENDPOINT):
        self.endpoint = endpoint

    def request(self, method: str, *args):
        return jsonrpcclient.request(self.endpoint, method, *args).data.result

    def get_block(self, hash: str) -> dict:
        return self.request('get_block', hash)

    def get_block_by_number(self, number: str) -> dict:
        return self.request('get_block_by_number', number)

    def get_header(self, hash: str) -> dict:
        return self.request('get_header', hash)

    def get_header_by_number(self, number: str) -> dict:
        return self.request('get_header_by_number', number)

    def get_transaction(self, hash: str) -> dict:
        return self.request('get_transaction', hash)

    def get_block_hash(self, number: str) -> str:
        return self.request('get_block_hash', number)

    def get_tip_header(self) -> dict:
        return self.request('get_tip_header')

    def get_tip_block_number(self) -> str:
        return self.request('get_tip_block_number')

    def get_current_epoch(self) -> dict:
        return self.request('get_current_epoch')

    def get_epoch_by_number(self, number: str) -> dict:
        return self.request('get_epoch_by_number', number)

    def get_cellbase_output_capacity_details(self, hash: str) -> dict:
        return self.request('get_cellbase_output_capacity_details', hash)


rpc = RPCClient()
