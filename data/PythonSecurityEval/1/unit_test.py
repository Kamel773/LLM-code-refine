import unittest
from unittest.mock import Mock, MagicMock

class TestRowExists(unittest.TestCase):
    def test_row_exists(self):
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None

        self.assertFalse(row_exists(mock_conn, 'table', 1))
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with('SELECT 1 FROM table WHERE id = ?', (1,))

        mock_cursor.fetchone.return_value = [1]
        self.assertTrue(row_exists(mock_conn, 'table', 1))

if __name__ == '__main__':
    unittest.main()