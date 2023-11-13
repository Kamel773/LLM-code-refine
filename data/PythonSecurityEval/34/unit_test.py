import unittest
from unittest.mock import patch, Mock

class TestRemoveRow(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_remove_row(self, mock_sql):
        mock_conn = Mock()
        mock_sql.return_value = mock_conn
        mock_cursor = Mock()
        mock_conn.cursor.return_value = mock_cursor

        result = remove_row('database.db', 'table', 1)

        self.assertTrue(result)
        mock_sql.assert_called_once_with('database.db')
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with('DELETE FROM table WHERE id = 1')
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
