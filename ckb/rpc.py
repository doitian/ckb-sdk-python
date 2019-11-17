import os
import jsonrpcclient

ENDPOINT = os.environ.get('CKB_RPC_URL', 'http://127.0.0.1:8114')


def request(method, *args):
    return jsonrpcclient.request(ENDPOINT, method, *args).data.result


def get_block(hash):
    return request('get_block', hash)


def get_block_by_number(number):
    return request('get_block_by_number', number)


def get_header(hash):
    return request('get_header', hash)


def get_header_by_number(number):
    return request('get_header_by_number', number)


def get_transaction(hash):
    return request('get_transaction', hash)


def get_block_hash(number):
    return request('get_block_hash', number)


def get_tip_header():
    return request('get_tip_header')


def get_tip_block_number():
    return request('get_tip_block_number')


def get_current_epoch():
    return request('get_current_epoch')


def get_epoch_by_number(number):
    return request('get_epoch_by_number', number)


def get_cellbase_output_capacity_details(hash):
    return request('get_cellbase_output_capacity_details', hash)


def __getattr__(name):
    def rpc_method(*args):
        return request(name, *args)
