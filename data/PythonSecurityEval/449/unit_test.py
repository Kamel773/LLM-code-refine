import unittest
from unittest.mock import patch, Mock
import bcrypt

class TestHashPassword(unittest.TestCase):
    @patch('bcrypt.gensalt')
    @patch('bcrypt.hashpw')
    def test_hash_password(self, mock_hashpw, mock_gensalt):
        mock_password = 'test_password'
        mock_salt = b'salt'
        mock_hashed = b'hashed_password'

        mock_gensalt.return_value = mock_salt
        mock_hashpw.return_value = mock_hashed

        from your_module import hash_password  # replace 'your_module' with the name of your module
        result = hash_password(mock_password)

        mock_gensalt.assert_called_once()
        mock_hashpw.assert_called_once_with(mock_password.encode('utf-8'), mock_salt)
        self.assertEqual(result, mock_hashed)

if __name__ == '__main__':
    unittest.main()