import unittest
from unittest.mock import patch, call
import your_module  # replace with the name of your module

class TestPasswordStorage(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_store_password(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        your_module.store_password('user', 'pass')
        mock_connect.assert_called_once_with('passwords.db')
        mock_cursor.execute.assert_called_once_with('INSERT INTO users (username, password) VALUES (?, ?)', ('user', 'pass'))
        mock_connect.return_value.commit.assert_called_once()
        mock_connect.return_value.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()