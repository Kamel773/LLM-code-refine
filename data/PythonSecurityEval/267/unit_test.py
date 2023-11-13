import unittest
from unittest.mock import patch

def encrypt_string(key, string):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(string.encode())
    return cipher_text

class TestEncryption(unittest.TestCase):
    @patch('cryptography.fernet.Fernet')
    def test_encrypt_string(self, mock_fernet):
        mock_fernet.return_value.encrypt.return_value = b'encrypted_string'
        key = Fernet.generate_key()
        string = 'test_string'
        result = encrypt_string(key, string)
        self.assertEqual(result, b'encrypted_string')
        mock_fernet.assert_called_once_with(key)
        mock_fernet.return_value.encrypt.assert_called_once_with(string.encode())

if __name__ == '__main__':
    unittest.main()