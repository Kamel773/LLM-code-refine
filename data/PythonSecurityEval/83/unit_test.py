import unittest
from unittest.mock import patch, Mock
from your_module_name import create_table  # Replace 'your_module_name' with the name of your module

class TestCreateTable(unittest.TestCase):

    @patch('your_module_name.sqlite3.connect')  # Replace 'your_module_name' with the name of your module
    def test_create_table(self, mock_connect):
        # Mocking the database connection and cursor
        mock_cursor = Mock()
        mock_connect.return_value.__enter__.return_value.cursor.return_value = mock_cursor

        # Test data
        db_name = "test.db"
        table_name = "test_table"
        columns = {
            "id": "INTEGER PRIMARY KEY",
            "name": "TEXT"
        }

        # Call the function
        create_table(db_name, table_name, columns)

        # Assert that the SQL command was executed
        mock_cursor.execute.assert_called_once()

if __name__ == "__main__":
    unittest.main()
