import unittest
from unittest.mock import patch, MagicMock
import bcrypt

class TestValidateCredentials(unittest.TestCase):
    @patch('pymysql.connect')
    def test_validate_credentials(self, mock_sql):
        # Mock the SQL connection and cursor
        mock_conn = mock_sql.return_value
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        # Mock the fetchone method to return a hashed password
        hashed_password = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt())
        mock_cursor.fetchone.return_value = [hashed_password]

        # Test the validate_credentials function
        result = validate_credentials('username', 'password')
        self.assertTrue(result)

        # Test with a wrong password
        result = validate_credentials('username', 'wrong_password')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()