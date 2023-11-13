import unittest
from unittest.mock import patch, Mock
import mysql.connector
import your_module  # replace with the name of the module where you defined the above function

class TestGetUserInfo(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_get_user_info(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = ('john_doe', 'John', 'Doe', 'john.doe@example.com')

        result = your_module.get_user_info('john_doe')

        self.assertEqual(result, ('john_doe', 'John', 'Doe', 'john.doe@example.com'))
        mock_cursor.execute.assert_called_once_with("SELECT * FROM users WHERE username = %s", ('john_doe',))
        mock_cursor.close.assert_called_once()
        mock_connect.return_value.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()