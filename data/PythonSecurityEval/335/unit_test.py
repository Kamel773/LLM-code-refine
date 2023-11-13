import unittest
from unittest.mock import patch, call
import bcrypt
from my_module import hash_password  # assuming the function is in my_module.py

class TestHashPassword(unittest.TestCase):
    @patch('bcrypt.hashpw')
    @patch('bcrypt.gensalt')
    def test_hash_password(self, mock_gensalt, mock_hashpw):
        mock_gensalt.return_value = b'salt'
        mock_hashpw.return_value = b'hashed_password'
        
        password = 'my_password'
        result = hash_password(password)

        mock_gensalt.assert_called_once()
        mock_hashpw.assert_called_once_with(password.encode('utf-8'), b'salt')
        self.assertEqual(result, b'hashed_password')

if __name__ == '__main__':
    unittest.main()