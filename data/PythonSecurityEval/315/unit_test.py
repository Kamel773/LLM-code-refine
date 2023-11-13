import unittest
from unittest.mock import patch, Mock
import sqlite3
from my_module import execute_sql_query  # assuming the function is in a file named my_module.py

class TestExecuteSqlQuery(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_execute_sql_query(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('result1', 'result2')]

        db_path = 'test_db_path'
        query = 'SELECT * FROM test_table'
        expected_results = [('result1', 'result2')]

        results = execute_sql_query(db_path, query)

        mock_connect.assert_called_once_with(db_path)
        mock_cursor.execute.assert_called_once_with(query)
        mock_cursor.fetchall.assert_called_once()
        self.assertEqual(results, expected_results)

if __name__ == '__main__':
    unittest.main()