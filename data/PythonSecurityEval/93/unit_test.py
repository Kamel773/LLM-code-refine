import unittest
from unittest.mock import patch, Mock
import sqlite3

class TestDatabaseFunction(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_execute_query(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        database = 'test.db'
        query = 'SELECT * FROM test_table'
        execute_query(database, query)

        mock_connect.assert_called_once_with(database)
        mock_cursor.execute.assert_called_once_with(query)
        mock_connect.return_value.commit.assert_called_once()
        mock_connect.return_value.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()