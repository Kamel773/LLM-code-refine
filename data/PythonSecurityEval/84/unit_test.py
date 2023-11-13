import unittest
from unittest.mock import patch, Mock

class TestPrintSQLiteTable(unittest.TestCase):

    @patch('sqlite3.connect')
    def test_print_sqlite_table(self, mock_connect):
        # Mocking the database connection and cursor
        mock_cursor = Mock()
        mock_connection = Mock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        
        # Mocking the fetchall method to return sample data
        mock_cursor.fetchall.return_value = [
            (1, "John Doe"),
            (2, "Jane Smith")
        ]

        # Call the function
        print_sqlite_table("dummy_path", "dummy_table")

        # Assert that the execute method was called with the correct SQL
        mock_cursor.execute.assert_called_once_with("SELECT * FROM dummy_table")

if __name__ == "__main__":
    unittest.main()
