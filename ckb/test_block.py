from unittest import TestCase

from ckb.block import transactions_root, proposals_hash, extra_hash, from_template
from ckb.header import header_hash

TEST_BLOCK = {'header': {'compact_target': '0x1a08a97e',
                         'dao': '0xc8f46621be95a12eb297027e08872300aee0b612a31800000077d034b838ff06',
                         'epoch': '0x6cf0388000000',
                         'hash': '0x04ca5b716e7463a6cffe5f978f1b68de727f623af77f8361241cb40e45b91de2',
                         'nonce': '0x5d9a05000000000000004a0b000001ba', 'number': '0x388',
                         'parent_hash': '0xf85598a6ea16e07c7b8dd612eccf7620f44b643a9faceb9f6efe7b6320282794',
                         'proposals_hash': '0xad225773c594929c7fd60b82b0cb300a42fe7c6235f40ca70ce6c35f69d4c061',
                         'timestamp': '0x16e77208628',
                         'transactions_root': '0xb7152b63347f20ac999a51a5a80e0a80c8a703dad686c2a65f084c9acd9f596c',
                         'extra_hash': '0x2d54b7e61b1a37d813ff4c1a13061973f6f5aed878b84765570228f7b17f7fe2',
                         'version': '0x0'},
              'proposals': ['0x1b61eeaeaed2ed6da110', '0x8b5f2f5033e4f78eb8d8', '0x63c4007a78cdbcfea1e6',
                            '0x18b874925241a7f55fb0'], 'transactions': [
        {'cell_deps': [], 'hash': '0x4e52431821736d3a37d8e5aeed67615c0c722a6f064b788acb2bd9322f6ed47a',
         'header_deps': [], 'inputs': [{'previous_output': {'index': '0xffffffff',
                                                            'tx_hash': '0x0000000000000000000000000000000000000000000000000000000000000000'},
                                        'since': '0x388'}], 'outputs': [{'capacity': '0x1ad925c507', 'lock': {
            'args': '0x0a486fb8f6fe60f76f001d6372da41be91172259',
            'code_hash': '0x9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8', 'hash_type': 'type'},
                                                                         'type': None}], 'outputs_data': ['0x'],
         'version': '0x0', 'witnesses': [
            '0x5a0000000c00000055000000490000001000000030000000310000009bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce801140000000a486fb8f6fe60f76f001d6372da41be911722590100000000']},
        {'cell_deps': [{'dep_type': 'dep_group', 'out_point': {'index': '0x0',
                                                               'tx_hash': '0x71a7ba8fc96349fea0ed3a5c47992e3b4084b031a42264a018e0072e8172e46c'}}],
         'hash': '0x47a1a0dc8308902a4b4f2a921c0199dfc2cfa23a163f26398d8dc1f3529b2a51', 'header_deps': [], 'inputs': [{
            'previous_output': {
                'index': '0x1',
                'tx_hash': '0xb4aa8c05207ec3e67e6408473cd93bdb89780864446bc7d6b6812b539c33d096'},
            'since': '0x0'}],
         'outputs': [{'capacity': '0x453b118f700', 'lock': {'args': '0x04e058890224cbb41e9fed2b10ce3ad20f014cda',
                                                            'code_hash': '0x9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8',
                                                            'hash_type': 'type'}, 'type': None},
                     {'capacity': '0x4bc772aa88c', 'lock': {'args': '0x6d9e5654ec5c0435dedd7fc869b66ba47eb60208',
                                                            'code_hash': '0x9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8',
                                                            'hash_type': 'type'}, 'type': None}],
         'outputs_data': ['0x', '0x'], 'version': '0x0', 'witnesses': [
            '0x5500000010000000550000005500000041000000f0ac95a3667c757b7e08783f7f0f78db47dfcd76511e42bf4f01435507fda0b8210a521fa12012aa70921f6e6e00dd2a7c1296512632f1dfb26957d9b409284701']},
        {'cell_deps': [{'dep_type': 'dep_group', 'out_point': {'index': '0x0',
                                                               'tx_hash': '0x71a7ba8fc96349fea0ed3a5c47992e3b4084b031a42264a018e0072e8172e46c'}}],
         'hash': '0x96a191bfeaf77fa351f9c5e59cc71893fd7d338317b0d5a766a9985216d84720', 'header_deps': [], 'inputs': [{
            'previous_output': {
                'index': '0x1',
                'tx_hash': '0x3ce938e5b12f707a0dd3122604f844509192bc6cb21377389ec8509683380839'},
            'since': '0x0'}],
         'outputs': [{'capacity': '0xba43b7400', 'lock': {'args': '0x3ff943b23be06ac76ac9de7c02ec0ede8286d47c',
                                                          'code_hash': '0x9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8',
                                                          'hash_type': 'type'}, 'type': None},
                     {'capacity': '0x6fc2336d0', 'lock': {'args': '0x56b1a3bed66c86b40151f2ba1bfe296032dd307b',
                                                          'code_hash': '0x9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8',
                                                          'hash_type': 'type'}, 'type': None}],
         'outputs_data': ['0x', '0x'], 'version': '0x0', 'witnesses': [
            '0x55000000100000005500000055000000410000000881853578e3ca9a3cb7a0faf5ba6b15f2a479c16f40e73f2e9b4552f900913c25da1d4ba34d16442e2c80d3ce62f72c7e0778a05f058e081c094ef4a865900700']}],
              'uncles': [{'header': {'compact_target': '0x1a08a97e',
                                     'dao': '0x408083509c95a12e28adc377088723001c2bf91a9c18000000a00cf2b338ff06',
                                     'epoch': '0x6cf0387000000',
                                     'hash': '0x300f8cc8d0e0c791e944484f2fd565bc01d775a6104180545087d7ec925c3e30',
                                     'nonce': '0x10d813d90000019d000000000e150200', 'number': '0x387',
                                     'parent_hash': '0xfbaa7c7ae19f2f99c971ae93d21a6f514d83e1528475c2ea1bd2e633574623f2',
                                     'proposals_hash': '0x2ee20468abe9e7766b5d4a88f2b8d3ebb65024bef3e463192776b9b35ac95315',
                                     'timestamp': '0x16e77154097',
                                     'transactions_root': '0x23d5696b2219ebca71b9371b29b646c1ea8fcdc3160c86c8602958a51f4ba53c',
                                     'extra_hash': '0x0000000000000000000000000000000000000000000000000000000000000000',
                                     'version': '0x0'},
                          'proposals': ['0x47a1a0dc8308902a4b4f', '0x88caab22953f4d3ff218', '0x52ca72462ba65e5af75e',
                                        '0x96a191bfeaf77fa351f9']}],
              'extension': None
              }

TEST_TEMPLATE = {'bytes_limit': '0x91c08', 'cellbase': {'cycles': None, 'data': {'cell_deps': [], 'header_deps': [],
                                                                                 'inputs': [{'previous_output': {
                                                                                     'index': '0xffffffff',
                                                                                     'tx_hash': '0x0000000000000000000000000000000000000000000000000000000000000000'},
                                                                                             'since': '0xc15'}],
                                                                                 'outputs': [
                                                                                     {'capacity': '0x19ff7b51b6',
                                                                                      'lock': {
                                                                                          'args': '0xc2baa1d5b45a3ad6452b9c98ad8e2cc52e5123c7',
                                                                                          'code_hash': '0x9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8',
                                                                                          'hash_type': 'type'},
                                                                                      'type': None}],
                                                                                 'outputs_data': ['0x'],
                                                                                 'version': '0x0', 'witnesses': [
        '0x590000000c00000055000000490000001000000030000000310000009bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce80114000000b5a27e6b01d309135b06089ce192a267ceada8ea00000000']},
                                                        'hash': '0x1237ec7aa972990a0a3e312c66dcad8c3e3809f25246ace455903a0cdd24f7cc'},
                 'compact_target': '0x1a11b985', 'current_time': '0x16e7e760599', 'cycles_limit': '0xd09dc300',
                 'dao': '0x2c2534963eb1a22efc2951da3c872300b87b10690d53000000ced287f44aff06',
                 'epoch': '0x7080546000001', 'number': '0xc15',
                 'parent_hash': '0x2ba74d90912f9e891f91ce0d75680fdb305346e15722cc20b7026bed2acf647c', 'proposals': [],
                 'transactions': [], 'uncles': [], 'uncles_count_limit': '0x2', 'version': '0x0', 'work_id': '0x0', 'extension': None}


class BlockTest(TestCase):
    def test_transactions_root(self):
        self.assertEqual(transactions_root(TEST_BLOCK['transactions']), TEST_BLOCK['header']['transactions_root'])

    def test_proposals_hash(self):
        self.assertEqual(proposals_hash(TEST_BLOCK['proposals']), TEST_BLOCK['header']['proposals_hash'])

    def test_extra_hash_example(self):
        self.assertEqual(extra_hash([], '0x626c6f636b202333'), '0xfbbfbaaa0afac7730f4a6102b376986f1f288f3eccb18e0d16d58422aab28aad')

    def test_extra_hash(self):
        self.assertEqual(extra_hash(TEST_BLOCK['uncles'], TEST_BLOCK['extension']), TEST_BLOCK['header']['extra_hash'])
    
    def test_from_template(self):
        block = from_template(TEST_TEMPLATE)
        block_hash = header_hash(block['header'])
        self.assertEqual(block_hash, '0x17f37d193286f34c3740c85e6e3f5e337e576339930fb361083827141b47511f')
