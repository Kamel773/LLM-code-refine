import unittest
from unittest.mock import patch, Mock
import sqlite3

class TestGetDictFromQuery(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_get_dict_from_query(self, mock_connect):
        # Mock the connection and cursor
        mock_cursor = Mock()
        mock_conn = Mock()

        # Set up the mock to return our connection and cursor when `connect` and `cursor` are called
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Set up the mock cursor's `fetchall` to return a list of sqlite3.Row-like objects
        rows = [sqlite3.Row(keys=("id", "name"), values=(1, "Test"))]
        mock_cursor.fetchall.return_value = rows

        # Now we can test our function
        from mymodule import get_dict_from_query  # assuming the function is in 'mymodule.py'

        result = get_dict_from_query("dummy_db_path", "SELECT * FROM dummy_table")
        expected_result = [{"id": 1, "name": "Test"}]

        self.assertEqual(result, expected_result)
        mock_cursor.execute.assert_called_once_with("SELECT * FROM dummy_table")

if __name__ == "__main__":
    unittest.main()
