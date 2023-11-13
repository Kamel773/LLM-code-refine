import unittest
from unittest.mock import patch, Mock
import my_module  # replace with the name of the module where your function is defined

class TestExecuteQuery(unittest.TestCase):
    @patch('my_module.sqlite3.connect')
    def test_execute_query(self, mock_connect):
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('result1', 'result2')]

        database = 'test.db'
        query = 'SELECT * FROM test'
        results = my_module.execute_query(database, query)

        mock_connect.assert_called_once_with(database)
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(query)
        mock_cursor.fetchall.assert_called_once()
        self.assertEqual(results, [('result1', 'result2')])

if __name__ == '__main__':
    unittest.main()