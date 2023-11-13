import unittest
from unittest.mock import patch, mock_open
from caesar_cipher import caesar_cipher_encrypt

class TestCaesarCipher(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="abc")
    def test_caesar_cipher_encrypt(self, mock_file):
        caesar_cipher_encrypt("test.txt", 1)
        mock_file.assert_called_with("test.txt", 'w')
        mock_file().write.assert_called_once_with("bcd")

if __name__ == '__main__':
    unittest.main()