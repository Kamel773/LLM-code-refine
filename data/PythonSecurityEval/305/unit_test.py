import unittest
from unittest.mock import patch, Mock
import bcrypt

class TestVerifyPassword(unittest.TestCase):
    @patch('bcrypt.checkpw')
    def test_verify_password(self, mock_checkpw):
        mock_hashed_password = b'$2b$12$SeV9gQz.5I77Zmk./.IeXeZ5A3F3nGZ6yB7Bj/DoS2t9z.7.pQ1ja'
        mock_password = 'password123'

        # Set up the mock
        mock_checkpw.return_value = True

        # Call the function with the mock parameters
        result = verify_password(mock_hashed_password, mock_password)

        # Assert that the function was called with the correct parameters
        mock_checkpw.assert_called_once_with(mock_password.encode('utf-8'), mock_hashed_password)

        # Assert that the function returned the correct result
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()