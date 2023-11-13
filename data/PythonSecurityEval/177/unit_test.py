import unittest
from unittest.mock import patch, MagicMock
from Crypto.Cipher import AES

class TestEncryption(unittest.TestCase):
    @patch('Crypto.Cipher.AES.new')
    @patch('Crypto.Util.Padding.pad')
    @patch('Crypto.Random.get_random_bytes')
    def test_generate_encryption_key(self, mock_random, mock_pad, mock_new):
        mock_random.return_value = b'random_key'
        mock_pad.return_value = b'padded_data'
        mock_cipher = MagicMock()
        mock_cipher.encrypt.return_value = b'encrypted_data'
        mock_new.return_value = mock_cipher

        data = 'test_data'
        key = b'test_key'
        result = generate_encryption_key(data, key)

        mock_random.assert_not_called()
        mock_pad.assert_called_once_with(data.encode(), AES.block_size)
        mock_new.assert_called_once_with(key, AES.MODE_CBC)
        mock_cipher.encrypt.assert_called_once_with(b'padded_data')
        self.assertEqual(result, (b'encrypted_data', mock_cipher.iv))

if __name__ == '__main__':
    unittest.main()