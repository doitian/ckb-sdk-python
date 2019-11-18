from .hash import ckb_hash
from .molecule import HeaderBuilder, extend_uint32, extend_uint64, extend_bytes_array, extend_bytes_fixvec
from .types import Transaction, TransactionTemplate, CellbaseTemplate, CellOutput, Script, HexH256


def extend_serialized_script(buffer: bytearray, script: Script) -> bytearray:
    # table Script
    # {
    #     code_hash: Byte32,
    #     hash_type: byte,
    #     args: Bytes,
    # }
    header = HeaderBuilder(buffer, 3)

    extend_bytes_array(buffer, script['code_hash'])
    header.finish_item()

    buffer.append(0 if script['hash_type'] == 'data' else 1)
    header.finish_item()

    extend_bytes_fixvec(buffer, script['args'])
    header.finish_item()

    return buffer


def extend_serialized_cell_output(buffer: bytearray, cell_output: CellOutput) -> bytearray:
    # table CellOutput
    # {
    #     capacity: Uint64,
    #     lock: Script,
    #     type_: ScriptOpt,
    # }
    header = HeaderBuilder(buffer, 3)

    extend_uint64(buffer, cell_output['capacity'])
    header.finish_item()

    extend_serialized_script(buffer, cell_output['lock'])
    header.finish_item()

    if 'type' in cell_output and cell_output['type'] is not None:
        extend_serialized_script(buffer, cell_output['type'])
    header.finish_item()

    return buffer


def extend_serialized_raw_transaction(buffer: bytearray, transaction: Transaction) -> bytearray:
    # table RawTransaction
    # {
    #     version: Uint32,
    #     cell_deps: CellDepVec,
    #     header_deps: Byte32Vec,
    #     inputs: CellInputVec,
    #     outputs: CellOutputVec,
    #     outputs_data: BytesVec,
    # }
    transaction_header = HeaderBuilder(buffer, 6)

    extend_uint32(buffer, transaction['version'])
    transaction_header.finish_item()

    # struct OutPoint
    # {
    #     tx_hash: Byte32,
    #     index: Uint32,
    # }

    buffer.extend(len(transaction['cell_deps']).to_bytes(4, 'little'))
    for cell_dep in transaction['cell_deps']:
        # struct CellDep
        # {
        #     out_point: OutPoint,
        #     dep_type: byte,
        # }
        extend_bytes_array(buffer, cell_dep['out_point']['tx_hash'])
        extend_uint32(buffer, cell_dep['out_point']['index'])
        buffer.append(0 if cell_dep['dep_type'] == 'code' else 1)
    transaction_header.finish_item()

    buffer.extend(len(transaction['header_deps']).to_bytes(4, 'little'))
    for header_dep in transaction['header_deps']:
        extend_bytes_array(buffer, header_dep)
    transaction_header.finish_item()

    buffer.extend(len(transaction['inputs']).to_bytes(4, 'little'))
    for input in transaction['inputs']:
        # struct CellInput
        # {
        #     since: Uint64,
        #     previous_output: OutPoint,
        # }
        extend_uint64(buffer, input['since'])
        extend_bytes_array(buffer, input['previous_output']['tx_hash'])
        extend_uint32(buffer, input['previous_output']['index'])
    transaction_header.finish_item()

    outputs_header = HeaderBuilder(buffer, len(transaction['outputs']))
    for output in transaction['outputs']:
        extend_serialized_cell_output(buffer, output)
        outputs_header.finish_item()
    transaction_header.finish_item()

    outputs_data_header = HeaderBuilder(buffer, len(transaction['outputs_data']))
    for output_data in transaction['outputs_data']:
        extend_bytes_fixvec(buffer, output_data)
        outputs_data_header.finish_item()
    transaction_header.finish_item()

    return buffer


def extend_serialized_transaction(buffer: bytearray, transaction: Transaction) -> bytearray:
    # table Transaction
    # {
    #     raw: RawTransaction,
    #     witnesses: BytesVec,
    # }
    transaction_header = HeaderBuilder(buffer, 2)

    extend_serialized_raw_transaction(buffer, transaction)
    transaction_header.finish_item()

    witnesses_header = HeaderBuilder(buffer, len(transaction['witnesses']))
    for witness in transaction['witnesses']:
        extend_bytes_fixvec(buffer, witness)
        witnesses_header.finish_item()
    transaction_header.finish_item()

    return buffer


def transaction_hash(transaction: Transaction) -> HexH256:
    buffer = bytearray()
    extend_serialized_raw_transaction(buffer, transaction)
    return ckb_hash(buffer)


def transaction_witness_hash(transaction: Transaction) -> HexH256:
    buffer = bytearray()
    extend_serialized_transaction(buffer, transaction)
    return ckb_hash(buffer)


def from_cellbase_template(template: CellbaseTemplate) -> Transaction:
    return template['data']


def from_template(template: TransactionTemplate) -> Transaction:
    return template['data']
