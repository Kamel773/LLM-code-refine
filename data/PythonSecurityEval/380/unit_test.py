import unittest
from unittest.mock import patch, Mock
import my_module  # replace with the name of the module that contains your function

class TestExecuteQuery(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_execute_query(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('result1', 'result2')]

        query = 'SELECT * FROM my_table'
        results = my_module.execute_query(query)

        mock_connect.assert_called_once_with('my_database.db')
        mock_cursor.execute.assert_called_once_with(query)
        mock_cursor.fetchall.assert_called_once()
        self.assertEqual(results, [('result1', 'result2')])

if __name__ == '__main__':
    unittest.main()