import unittest
from unittest.mock import patch, Mock
import my_module  # replace with the name of the module where insert_user is defined

class TestInsertUser(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_insert_user(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        my_module.insert_user('test_user', 'test_password')

        mock_connect.assert_called_once_with('my_database.db')
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            ('test_user', 'test_password')
        )
        mock_connect.return_value.commit.assert_called_once()
        mock_connect.return_value.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()