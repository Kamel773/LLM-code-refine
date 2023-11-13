import unittest
from unittest.mock import patch, Mock
import sqlite3
from your_module import modify_database  # replace 'your_module' with the name of your module

class TestModifyDatabase(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_modify_database(self, mock_sql):
        mock_conn = Mock()
        mock_sql.return_value = mock_conn
        mock_cursor = Mock()
        mock_conn.cursor.return_value = mock_cursor

        modify_database('test.db')

        mock_sql.assert_called_once_with('test.db')
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_any_call('''CREATE TABLE users
                 (name text, email text)''')
        mock_cursor.execute.assert_any_call("INSERT INTO users VALUES ('John Doe','john.doe@example.com')")
        mock_conn.commit.assert_called_once()
        mock_cursor.execute.assert_any_call('SELECT * FROM users')
        mock_cursor.fetchall.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()