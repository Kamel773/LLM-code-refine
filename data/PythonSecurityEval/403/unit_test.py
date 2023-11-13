import unittest
from unittest.mock import patch, Mock
import sqlite3
import your_module  # replace with the name of the module where you defined the update_row function

class TestUpdateRow(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_update_row(self, mock_sqlite3_connect):
        mock_conn = Mock()
        mock_cursor = Mock()

        mock_sqlite3_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        your_module.update_row("company.db", "employees", "salary", 50000, "id = 1")

        mock_sqlite3_connect.assert_called_once_with("company.db")
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with("UPDATE employees SET salary = ? WHERE id = 1", (50000,))
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()