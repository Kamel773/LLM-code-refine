import unittest
from unittest.mock import patch
import sqlite3
import your_module  # replace with the name of your module

class TestExecuteQuery(unittest.TestCase):
    @patch('your_module.sqlite3.connect')
    @patch('your_module.input', return_value='SELECT * FROM table')
    def test_execute_query(self, input, connect):
        mock_conn = connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        your_module.execute_query()

        mock_cursor.execute.assert_called_once_with('SELECT * FROM table')
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()