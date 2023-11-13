import unittest
from unittest.mock import patch, MagicMock
import bcrypt

class TestPasswordHashing(unittest.TestCase):
    @patch('bcrypt.gensalt')
    @patch('bcrypt.hashpw')
    def test_hash_password(self, mock_hashpw, mock_gensalt):
        mock_password = 'test_password'
        mock_salt = b'salt'
        mock_hashed_password = b'hashed_password'

        # Set up the mock functions
        mock_gensalt.return_value = mock_salt
        mock_hashpw.return_value = mock_hashed_password

        # Call the function with the mock password
        result = hash_password(mock_password)

        # Check that the mock functions were called with the correct arguments
        mock_gensalt.assert_called_once()
        mock_hashpw.assert_called_once_with(mock_password.encode(), mock_salt)

        # Check that the function returned the correct result
        self.assertEqual(result, mock_hashed_password)

if __name__ == '__main__':
    unittest.main()