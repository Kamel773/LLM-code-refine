import unittest
from unittest.mock import mock_open, patch
from my_module import encrypt_file  # assuming the function is in a module named my_module

class TestEncryptFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='abc')
    def test_encrypt_file(self, mock_file):
        encrypt_file('dummy_path', 3)
        mock_file.assert_called_once_with('dummy_path', 'w')
        mock_file().write.assert_called_once_with('def')

if __name__ == '__main__':
    unittest.main()