import unittest
from unittest.mock import patch, MagicMock
import my_module  # replace with the name of the module where execute_query is defined

class TestExecuteQuery(unittest.TestCase):
    @patch('pymysql.connect')
    def test_execute_query(self, mock_sql):
        # Set up the mock
        mock_cursor = MagicMock()
        mock_sql.return_value.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [{'id': 1, 'name': 'Test'}]

        # Call the function with a test query
        result = my_module.execute_query('SELECT * FROM test')

        # Check that the function made the expected calls
        mock_sql.assert_called_once_with(host='localhost',
                                         user='user',
                                         password='passwd',
                                         db='db',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
        mock_cursor.execute.assert_called_once_with('SELECT * FROM test')
        mock_cursor.fetchall.assert_called_once()

        # Check that the function returned the expected result
        self.assertEqual(result, [{'id': 1, 'name': 'Test'}])

if __name__ == '__main__':
    unittest.main()