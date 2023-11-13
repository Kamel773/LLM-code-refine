import unittest
from unittest.mock import patch, MagicMock
import os

class TestHashPassword(unittest.TestCase):
    @patch('os.urandom')
    @patch('hashlib.pbkdf2_hmac')
    def test_hash_password(self, mock_hash, mock_urandom):
        # Set up the mock objects
        mock_salt = os.urandom(16)
        mock_urandom.return_value = mock_salt
        mock_hash.return_value = b'somehashedpassword'

        # Call the function with a test password
        salt, hashed_password = hash_password('testpassword')

        # Check that the mock objects were called with the correct arguments
        mock_urandom.assert_called_once_with(16)
        mock_hash.assert_called_once_with('sha256', 'testpassword'.encode('utf-8'), mock_salt, 100000)

        # Check that the function returned the correct values
        self.assertEqual(salt, mock_salt)
        self.assertEqual(hashed_password, b'somehashedpassword')

if __name__ == '__main__':
    unittest.main()