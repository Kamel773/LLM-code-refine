import unittest
from unittest.mock import patch, MagicMock
from Crypto.Random import get_random_bytes

class TestEncryption(unittest.TestCase):
    @patch('main.encrypt_data')
    @patch('main.decrypt_data')
    def test_encryption_decryption(self, mock_decrypt, mock_encrypt):
        key = get_random_bytes(16)
        original_data = 'Sensitive data'
        mock_encrypt.return_value = encrypt_data(original_data, key)
        encrypted_data = mock_encrypt(original_data, key)
        mock_decrypt.return_value = decrypt_data(*encrypted_data, key)
        decrypted_data = mock_decrypt(*encrypted_data, key)
        self.assertEqual(original_data, decrypted_data)

if __name__ == '__main__':
    unittest.main()