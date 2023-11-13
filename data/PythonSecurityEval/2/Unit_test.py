import unittest
from unittest.mock import patch, MagicMock, mock_open

class TestCounter(unittest.TestCase):

    @patch('sqlite3.connect')
    def test_counter(self, mock_sql):
        # Set up the mock to return a specific count
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = [10]  # Assume there are 10 rows
        mock_conn.cursor.return_value = mock_cursor
        mock_sql.return_value = mock_conn

        # Call the function with a test database file and table name
        result = counter('test.db', 'test_table')

        # Assert that the function correctly counted the rows
        self.assertEqual(result, 10)
        mock_sql.assert_called_once_with('test.db')
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with('SELECT COUNT(*) FROM test_table')
        mock_cursor.fetchone.assert_called_once()

if __name__ == '__main__':
    unittest.main()