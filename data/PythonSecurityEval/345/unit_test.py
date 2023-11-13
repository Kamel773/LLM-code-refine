import unittest
from unittest.mock import patch, Mock
import bcrypt

class TestVerifyPassword(unittest.TestCase):
    @patch('bcrypt.checkpw')
    def test_verify_password(self, mock_checkpw):
        mock_checkpw.return_value = True
        result = verify_password(b'hashed_password', 'password')
        self.assertTrue(result)
        mock_checkpw.assert_called_once_with('password'.encode('utf-8'), b'hashed_password')

if __name__ == '__main__':
    unittest.main()