import unittest
from unittest.mock import patch, Mock

class TestGetRandomRecords(unittest.TestCase):

    @patch('sqlite3.connect')
    def test_get_random_records(self, mock_connect):
        # Mock the database connection and cursor
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        # Mock the return value for fetchall
        mock_cursor.fetchall.return_value = [('record1',), ('record2',), ...]  # Add as many mock records as needed

        # Call the function
        records = get_random_records('mock_db_path', 'mock_table_name')

        # Assert the function calls
        mock_connect.assert_called_once_with('mock_db_path')
        mock_cursor.execute.assert_called_once_with('SELECT * FROM mock_table_name ORDER BY RANDOM() LIMIT 100;')
        mock_cursor.fetchall.assert_called_once()

        # Assert the return value
        self.assertEqual(records, [('record1',), ('record2',), ...])  # Match with the mock records

if __name__ == '__main__':
    unittest.main()
