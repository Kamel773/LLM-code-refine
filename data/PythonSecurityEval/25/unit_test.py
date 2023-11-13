import unittest
from unittest.mock import Mock, patch
import mysql.connector

class TestInsertData(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_insert_data(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        db_config = {
            'user': 'test_user',
            'password': 'test_password',
            'host': 'localhost',
            'database': 'test_db'
        }
        table_name = 'test_table'
        data = {
            'column1': 'value1',
            'column2': 'value2'
        }
        
        # Call the function we're testing
        insert_data(db_config, table_name, data)

        # Create the expected SQL and values
        expected_sql = "INSERT INTO test_table (column1, column2) VALUES (%s, %s)"
        expected_values = ['value1', 'value2']
        
        # Assert that the SQL query was executed correctly
        mock_cursor.execute.assert_called_once_with(expected_sql, expected_values)
        # Assert that the changes were committed
        mock_connect.return_value.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
