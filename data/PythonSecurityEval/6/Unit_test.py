import unittest
from unittest.mock import Mock, patch

class TestInsertNull(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_insert_null(self, mock_connect):
        mock_conn = Mock()
        mock_cursor = Mock()

        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        db_name = 'test.db'
        table_name = 'test_table'
        column_name = 'test_column'

        insert_null(db_name, table_name, column_name)

        mock_connect.assert_called_once_with(db_name)
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            f"INSERT INTO {table_name} ({column_name}) VALUES (?)", 
            (None,)
        )
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()