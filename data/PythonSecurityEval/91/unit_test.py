import unittest
from unittest.mock import patch, Mock
import sqlite3

# Assuming the function insert_into_db is in a module named my_module
# from my_module import insert_into_db

class TestInsertIntoDB(unittest.TestCase):

    @patch('sqlite3.connect')
    def test_insert_into_db(self, mock_connect):
        # Mock database connection and cursor
        mock_conn = Mock(spec=sqlite3.Connection)
        mock_cursor = Mock(spec=sqlite3.Cursor)
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Test data
        db_path = 'test.db'
        table_name = 'test_table'
        data_dict = {'name': 'John', 'age': 30}

        # Call the function
        insert_into_db(db_path, table_name, data_dict)

        # Assert that the expected SQL query was executed
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO test_table (name, age) VALUES (?, ?)", 
            ('John', 30)
        )
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
