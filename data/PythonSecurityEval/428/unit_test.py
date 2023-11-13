import unittest
from unittest.mock import patch, ANY
import sqlite3

class TestInsertIntoDb(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_insert_into_db(self, mock_connect):
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        insert_into_db('test_input')

        mock_connect.assert_called_once_with('my_database.db')
        mock_cursor.execute.assert_called_once_with("INSERT INTO my_table (user_input) VALUES (?)", ('test_input',))
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()