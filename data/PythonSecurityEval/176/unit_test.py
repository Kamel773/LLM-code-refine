import unittest
from unittest.mock import patch, MagicMock
import hashlib
import binascii

class TestHashPassword(unittest.TestCase):
    @patch('hashlib.pbkdf2_hmac')
    @patch('binascii.hexlify')
    def test_hash_password(self, mock_hexlify, mock_pbkdf2_hmac):
        # Arrange
        mock_password = 'password'
        mock_salt = 'salt'
        mock_pbkdf2_hmac.return_value = b'hashed_password'
        mock_hexlify.return_value = b'hexlified_password'
        
        # Act
        result = hash_password(mock_password, mock_salt)
        
        # Assert
        mock_pbkdf2_hmac.assert_called_once_with('sha256', mock_password.encode(), mock_salt.encode(), 100000)
        mock_hexlify.assert_called_once_with(b'hashed_password')
        self.assertEqual(result, 'hexlified_password')

if __name__ == '__main__':
    unittest.main()