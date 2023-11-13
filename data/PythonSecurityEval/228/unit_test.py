import unittest
from unittest.mock import patch, Mock

class TestCreateUser(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_create_user(self, mock_sql):
        mock_conn = Mock()
        mock_sql.return_value = mock_conn
        mock_cursor = Mock()
        mock_conn.cursor.return_value = mock_cursor

        create_user('testuser', 'testpassword')  # replace with the name of your module

        mock_sql.assert_called_once_with('users.db')
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once()
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()