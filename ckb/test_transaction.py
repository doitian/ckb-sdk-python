from unittest import TestCase

from .transaction import transaction_hash, transaction_witness_hash

TEST_TRANSACTION = {'cell_deps': [], 'hash': '0xa09fdc7b0751b8dd11947bbba229ad16d825dfad18d31bc662f048233e2251f3',
                    'header_deps': [], 'inputs': [{'previous_output': {'index': '0xffffffff',
                                                                       'tx_hash': '0x0000000000000000000000000000000000000000000000000000000000000000'},
                                                   'since': '0xb0e'}], 'outputs': [{'capacity': '0x19ff7d6f4e',
                                                                                    'lock': {
                                                                                        'args': '0xdde7801c073dfb3464c7b1f05b806bb2bbb84e99',
                                                                                        'code_hash': '0x9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8',
                                                                                        'hash_type': 'type'},
                                                                                    'type': None}],
                    'outputs_data': ['0x'], 'version': '0x0', 'witnesses': [
        '0x5d0000000c00000055000000490000001000000030000000310000009bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce80114000000dde7801c073dfb3464c7b1f05b806bb2bbb84e990400000000000000']}


class TransactionTest(TestCase):
    def test_transaction_hash(self):
        self.assertEqual(transaction_hash(TEST_TRANSACTION), TEST_TRANSACTION['hash'])

    def test_transaction_witness_hash(self):
        self.assertEqual(transaction_witness_hash(TEST_TRANSACTION),
                         '0xa94ece15a2c5495f0aaf6e3e2fc33661aa6822e6badbc2fbe75e8452a754061a')
