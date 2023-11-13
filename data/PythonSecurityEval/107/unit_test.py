import unittest
from unittest.mock import patch, Mock
import sqlite3

class TestUpdateRow(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_update_row(self, mock_connect):
        mock_conn = Mock()
        mock_cursor = Mock()

        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        db_name = 'test.db'
        table_name = 'test_table'
        column_name = 'test_column'
        new_value = 'new_value'
        condition = 'id = 1'

        update_row(db_name, table_name, column_name, new_value, condition)

        mock_connect.assert_called_once_with(db_name)
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(f"UPDATE {table_name} SET {column_name} = ? WHERE {condition}", (new_value,))
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()