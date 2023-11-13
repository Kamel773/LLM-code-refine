import unittest
from unittest.mock import patch, Mock
import sqlite3

class TestGetTableNames(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_get_table_names(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('table1',), ('table2',), ('table3',)]

        result = get_table_names('test_db')

        mock_connect.assert_called_once_with('test_db')
        mock_cursor.execute.assert_called_once_with("SELECT name FROM sqlite_master WHERE type='table';")
        self.assertEqual(result, ['table1', 'table2', 'table3'])

if __name__ == '__main__':
    unittest.main()