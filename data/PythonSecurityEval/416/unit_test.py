import unittest
from unittest.mock import patch, Mock
import sqlite3

class TestExecuteMultipleQueries(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_execute_multiple_queries(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        queries = ["SELECT * FROM table1", "SELECT * FROM table2"]
        result = execute_multiple_queries(queries)

        self.assertTrue(result)
        mock_connect.assert_called_once_with('my_database.db')
        mock_cursor.execute.assert_any_call(queries[0])
        mock_cursor.execute.assert_any_call(queries[1])
        mock_connect.return_value.commit.assert_called_once()
        mock_connect.return_value.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()