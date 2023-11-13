import unittest
from unittest.mock import patch, Mock

class TestGetColumnNames(unittest.TestCase):

    @patch('sqlite3.connect')
    def test_get_column_names(self, mock_connect):
        # Mock the SQLite connection and cursor
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = [(0, 'id', 'INT', 0, None, 0), (1, 'name', 'TEXT', 0, None, 0)]
        mock_connection = Mock()
        mock_connection.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_connection

        # Test the function
        columns = get_column_names('dummy_path', 'dummy_table')
        self.assertEqual(columns, ['id', 'name'])

if __name__ == '__main__':
    unittest.main()