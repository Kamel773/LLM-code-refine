import unittest
from unittest.mock import mock_open, patch, call

class TestDecryptFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='encrypted_text')
    def test_decrypt_file(self, mock_open):
        decrypt_file('file_path', 3)

        # Check if the file was opened in read mode
        mock_open.assert_called_once_with('file_path', 'r')

        # Check if the read method was called
        mock_open().read.assert_called_once()

        # Check if the file was opened in write mode
        mock_open.assert_has_calls([call('file_path', 'w')])

        # Check if the write method was called with the decrypted text
        mock_open().write.assert_called_once_with('decrypted_text')

if __name__ == '__main__':
    unittest.main()