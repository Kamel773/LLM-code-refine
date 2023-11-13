import unittest
from unittest.mock import patch, Mock
from your_module import insert_json_to_db  # replace 'your_module' with the actual module name

class TestInsertJsonToDb(unittest.TestCase):
    @patch('psycopg2.connect')
    def test_insert_json_to_db(self, mock_connect):
        # Mock database connection and cursor
        mock_conn = Mock()
        mock_cur = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur

        # Test data
        json_str = '[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]'
        table_name = "test_table"
        db_name = "test_db"
        user = "test_user"
        password = "test_password"

        # Call the function
        insert_json_to_db(json_str, table_name, db_name, user, password)

        # Assert that the functions were called with the correct arguments
        mock_connect.assert_called_once_with(dbname=db_name, user=user, password=password, host="localhost", port="5432")
        mock_conn.cursor.assert_called_once()
        mock_cur.execute.assert_called_once_with("INSERT INTO test_table (name, age) VALUES (%s, %s)", [('John', 30), ('Jane', 25)])
        mock_conn.commit.assert_called_once()
        mock_cur.close.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()