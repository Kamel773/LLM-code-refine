import unittest
from unittest.mock import patch, Mock
import sqlite3

class TestCheckRowExists(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_check_row_exists(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('test',)]

        result = check_row_exists('test.db', 'test_table', 'id=1')

        self.assertTrue(result)
        mock_connect.assert_called_once_with('test.db')
        mock_cursor.execute.assert_called_once_with('SELECT * FROM test_table WHERE id=1')
        mock_cursor.fetchall.assert_called_once()

if __name__ == '__main__':
    unittest.main()