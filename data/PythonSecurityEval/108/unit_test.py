import unittest
from unittest.mock import patch, Mock
import sqlite3

class TestRemoveTopRow(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_remove_top_row(self, mock_connect):
        mock_conn = Mock()
        mock_cursor = Mock()

        # Set up the mock objects
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = [1]

        # Call the function with the mock objects
        remove_top_row('test_db', 'test_table')

        # Check if the correct SQL commands were executed
        mock_cursor.execute.assert_any_call("SELECT rowid FROM test_table ORDER BY rowid ASC LIMIT 1")
        mock_cursor.execute.assert_any_call("DELETE FROM test_table WHERE rowid = ?", (1,))
        mock_conn.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()