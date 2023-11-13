import unittest
from unittest.mock import patch, mock_open
import os

class TestJsonToSQLite(unittest.TestCase):
    
    @patch('sqlite3.connect')
    def test_json_to_sqlite(self, mock_connect):
        # Mock data
        mock_json = '[{"name": "John", "age": "25"}, {"name": "Doe", "age": "30"}]'
        mock_db_name = "test.db"
        
        # Call the function
        json_to_sqlite(mock_json, mock_db_name)
        
        # Assert that the connect method was called with the correct db name
        mock_connect.assert_called_once_with(mock_db_name)
        
        # Assert that the cursor method was called
        mock_cursor = mock_connect.return_value.cursor.return_value
        self.assertTrue(mock_cursor.execute.called)
        
        # Assert that the commit method was called
        mock_connect.return_value.commit.assert_called_once()
        
        # Assert that the close method was called
        mock_connect.return_value.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()
