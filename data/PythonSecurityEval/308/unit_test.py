import unittest
from unittest.mock import patch, mock_open
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

class TestDecryptFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data=b'encrypted data')
    @patch('Crypto.Cipher.AES.new')
    @patch('Crypto.Util.Padding.unpad')
    def test_decrypt_file(self, mock_unpad, mock_new, mock_open):
        mock_cipher = mock_new.return_value
        mock_cipher.decrypt.return_value = b'padded plaintext'
        mock_unpad.return_value = b'plaintext'

        decrypt_file('input_file', 'output_file', 'key')

        mock_open.assert_called_once_with('input_file', 'rb')
        mock_new.assert_called_once_with('key', AES.MODE_ECB)
        mock_cipher.decrypt.assert_called_once_with(b'encrypted data')
        mock_unpad.assert_called_once_with(b'padded plaintext', AES.block_size)
        mock_open().write.assert_called_once_with(b'plaintext')

if __name__ == '__main__':
    unittest.main()