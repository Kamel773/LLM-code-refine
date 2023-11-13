import unittest
from unittest.mock import patch, Mock
import sqlite3
from my_module import execute_sql_query  # assuming the function is in my_module.py

class TestExecuteSqlQuery(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_execute_sql_query(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        execute_sql_query('SELECT * FROM my_table')

        mock_connect.assert_called_once_with('my_database.db')
        mock_cursor.execute.assert_called_once_with('SELECT * FROM my_table')
        mock_connect.return_value.commit.assert_called_once()
        mock_connect.return_value.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()