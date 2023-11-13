import unittest
from unittest.mock import patch, Mock
import sqlite3

class TestSqlToJson(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_sql_to_json(self, mock_sql):
        mock_conn = Mock()
        mock_cursor = Mock()
        
        mock_sql.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        
        test_data = [('John', 30), ('Jane', 25)]
        mock_cursor.fetchall.return_value = test_data
        mock_cursor.description = [('Name', None, None, None, None, None, None), 
                                   ('Age', None, None, None, None, None, None)]
        
        expected_result = json.dumps([{"Name": "John", "Age": 30}, {"Name": "Jane", "Age": 25}])
        
        result = sql_to_json("test_db", "test_table")
        
        self.assertEqual(result, expected_result)
        mock_sql.assert_called_once_with('test_db')
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with('SELECT * FROM test_table;')

if __name__ == '__main__':
    unittest.main()