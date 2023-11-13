import unittest
from unittest.mock import patch, Mock

class TestUpdateMultipleRows(unittest.TestCase):

    @patch('sqlite3.connect')
    def test_update_multiple_rows(self, mock_connect):
        # Mocking the database connection and cursor
        mock_cursor = Mock()
        mock_cursor.rowcount = 2
        mock_connect.return_value.__enter__.return_value.cursor.return_value = mock_cursor
        
        # Test parameters
        database_path = "test.db"
        table_name = "test_table"
        set_columns_values = {"name": "John"}
        where_conditions = [{"id": 1}, {"id": 2}]
        
        # Call the function
        updated_rows = update_multiple_rows(database_path, table_name, set_columns_values, where_conditions)
        
        # Assertions
        self.assertEqual(updated_rows, 2)
        mock_cursor.execute.assert_called_once()

if __name__ == "__main__":
    unittest.main()
