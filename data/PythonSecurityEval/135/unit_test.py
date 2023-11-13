import unittest
from unittest.mock import patch, MagicMock
import pymysql

class TestRemoveUser(unittest.TestCase):
    @patch('pymysql.connect')
    def test_remove_user(self, mock_sql):
        mock_db = MagicMock()
        mock_sql.return_value = mock_db

        mock_cursor = MagicMock()
        mock_db.cursor.return_value = mock_cursor

        remove_user(1)  # replace with the name of your module

        mock_sql.assert_called_once_with("localhost", "testuser", "testpassword", "testdb")
        mock_db.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with("DELETE FROM users WHERE id = %s", (1,))
        mock_db.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()