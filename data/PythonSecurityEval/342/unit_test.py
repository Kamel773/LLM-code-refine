import unittest
from unittest.mock import patch

def decrypt_string(encrypted_string, key):
    cipher_suite = Fernet(key)
    decoded_text = cipher_suite.decrypt(encrypted_string)
    return decoded_text.decode("utf-8")

class TestDecryptString(unittest.TestCase):
    @patch('cryptography.fernet.Fernet')
    def test_decrypt_string(self, mock_fernet):
        mock_fernet.return_value.decrypt.return_value = b'decrypted string'
        key = Fernet.generate_key()
        encrypted_string = Fernet(key).encrypt(b'encrypted string')
        result = decrypt_string(encrypted_string, key)
        self.assertEqual(result, 'decrypted string')

if __name__ == '__main__':
    unittest.main()