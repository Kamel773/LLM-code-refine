import unittest
from unittest.mock import patch, MagicMock
from Crypto.Cipher import AES

class TestEncryptData(unittest.TestCase):
    @patch('Crypto.Random.get_random_bytes')
    @patch('Crypto.Cipher.AES.new')
    def test_encrypt_data(self, mock_new, mock_get_random_bytes):
        mock_get_random_bytes.return_value = b'1234567890123456'
        mock_cipher = MagicMock()
        mock_new.return_value = mock_cipher
        mock_cipher.encrypt.return_value = b'encrypted'
        
        data = 'test data'
        result = encrypt_data(data)
        
        mock_get_random_bytes.assert_called_once_with(16)
        mock_new.assert_called_once_with(b'1234567890123456', AES.MODE_CBC)
        mock_cipher.encrypt.assert_called_once()
        self.assertEqual(result, (b'encrypted', mock_cipher.iv))

if __name__ == '__main__':
    unittest.main()