from unittest import TestCase

from .header import header_hash, pow_hash

TEST_HEADER = {'compact_target': '0x1a08a97e',
               'dao': '0x920c75d0a1a8a12e071127fb0b8723003947ac75871c000000a3e044a53bff06', 'epoch': '0x6cf0417000000',
               'hash': '0xc3ffedc5143d516ab35993667a8e243491b879ae19b8605d74b20f08a4b72b52',
               'nonce': '0x87829506000005a10000000001470500', 'number': '0x417',
               'parent_hash': '0x664ff8295293522f79db8e421f919aab35f72ce1cd60e7b93e5f1d27977010ee',
               'proposals_hash': '0x0000000000000000000000000000000000000000000000000000000000000000',
               'timestamp': '0x16e783b79fd',
               'transactions_root': '0x445dc8adada6feaf5275f9e31a1e9044588de0eaf73e8afdc21cbf07f79bf87f',
               'extra_hash': '0x0000000000000000000000000000000000000000000000000000000000000000', 'version': '0x0'}


class HeaderTest(TestCase):
    def test_header_hash(self):
        self.assertEqual(header_hash(TEST_HEADER), TEST_HEADER['hash'])

    def test_pow_hash(self):
        self.assertEqual(pow_hash(TEST_HEADER), '0x633dd3a34be2355055b020ea49fe01d8666a4756bda4aac0b6f02746fcdf398e')
