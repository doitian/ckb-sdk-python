from unittest import TestCase

from . import cbmt
from .hash import H256_ZEROS
from .hex_coder import hex_from_bytes, hex_to_bytes


def merge(a, b):
    return hex_from_bytes(cbmt.merge(hex_to_bytes(a), hex_to_bytes(b)))


TEST_ITEMS = [
    '0x2751b0faa8b0b63ffb74e0de06b05370c583e9f0befabdde3dc03332fbb58f57',
    '0x88ac55ef5d947349b937cb3f307dd7b1650847f5389dcc1ff999df34c61ee9f9',
    '0xfc337768c8817bd291eaa770550b07c28c3aec01d0046ac654a8098ee9c433a5',
    '0xb92f8fa579cf33d1085b805f6ec877c6600b7f7a5ac3433aedec87a31f69dfa1',
    '0xea29021190bc3891016d1a69b3d7ea44a33b62ebe9717c458b98c7b5e4227d8f',
    '0xc7b99222cb6647bcb28af98f70c6417b73e4701088ab82cc988f857b880ca055',
    '0x4c493215c235f3546b66aaec1eda68044c4ab0ada549433356789596108a7cda',
    '0xdf2597213b983c0d4f7fd426e38128bb609ff58e0b05c6e8f2c7c3ea041e623d',
    '0x65b6a53f6aa7413ece5b100e2e2c203bef6613262815ea621348427a9941d884'
]


class TestCbmt(TestCase):
    def test_empty_tree(self):
        self.assertEqual(cbmt.cbmt_root([]), H256_ZEROS)

    def test_single_item(self):
        self.assertEqual(cbmt.cbmt_root(TEST_ITEMS[0:1]), TEST_ITEMS[0])

    def test_two_items(self):
        self.assertEqual(cbmt.cbmt_root(TEST_ITEMS[0:2]), merge(TEST_ITEMS[0], TEST_ITEMS[1]))

    def test_three_items(self):
        self.assertEqual(cbmt.cbmt_root(TEST_ITEMS[0:3]), merge(merge(TEST_ITEMS[1], TEST_ITEMS[2]), TEST_ITEMS[0]))

    def test_four_items(self):
        self.assertEqual(cbmt.cbmt_root(TEST_ITEMS[0:4]),
                         merge(merge(TEST_ITEMS[0], TEST_ITEMS[1]), merge(TEST_ITEMS[2], TEST_ITEMS[3])))

    def test_five_items(self):
        self.assertEqual(cbmt.cbmt_root(TEST_ITEMS[0:5]),
                         merge(merge(merge(TEST_ITEMS[3], TEST_ITEMS[4]), TEST_ITEMS[0]),
                               merge(TEST_ITEMS[1], TEST_ITEMS[2])))

    def test_six_items(self):
        self.assertEqual(cbmt.cbmt_root(TEST_ITEMS[0:6]),
                         merge(merge(merge(TEST_ITEMS[2], TEST_ITEMS[3]), merge(TEST_ITEMS[4], TEST_ITEMS[5])),
                               merge(TEST_ITEMS[0], TEST_ITEMS[1])))

    def test_seven_items(self):
        self.assertEqual(cbmt.cbmt_root(TEST_ITEMS[0:7]),
                         merge(merge(merge(TEST_ITEMS[1], TEST_ITEMS[2]), merge(TEST_ITEMS[3], TEST_ITEMS[4])),
                               merge(merge(TEST_ITEMS[5], TEST_ITEMS[6]), TEST_ITEMS[0])))

    def test_eight_items(self):
        self.assertEqual(cbmt.cbmt_root(TEST_ITEMS[0:8]),
                         merge(merge(merge(TEST_ITEMS[0], TEST_ITEMS[1]), merge(TEST_ITEMS[2], TEST_ITEMS[3])),
                               merge(merge(TEST_ITEMS[4], TEST_ITEMS[5]), merge(TEST_ITEMS[6], TEST_ITEMS[7]))))

    def test_nine_items(self):
        self.assertEqual(cbmt.cbmt_root(TEST_ITEMS[0:9]),
                         merge(merge(merge(merge(TEST_ITEMS[7], TEST_ITEMS[8]), TEST_ITEMS[0]),
                                     merge(TEST_ITEMS[1], TEST_ITEMS[2])),
                               merge(merge(TEST_ITEMS[3], TEST_ITEMS[4]), merge(TEST_ITEMS[5], TEST_ITEMS[6]))))
