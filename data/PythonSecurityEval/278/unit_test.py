import unittest
from unittest.mock import patch, call

class TestEncryption(unittest.TestCase):
    @patch('module_name.caesar_encrypt')
    def test_caesar_encrypt(self, mock_caesar_encrypt):
        text = "HELLO"
        shift = 3
        module_name.caesar_encrypt(text, shift)
        mock_caesar_encrypt.assert_called_with(text, shift)

if __name__ == '__main__':
    unittest.main()