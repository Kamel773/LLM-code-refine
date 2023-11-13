import unittest
from unittest.mock import patch, Mock
import your_module  # replace with the name of your module

class TestExecuteQuery(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_execute_query(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        your_module.execute_query('test.db', 'SELECT * FROM test')

        mock_connect.assert_called_once_with('test.db')
        mock_cursor.execute.assert_called_once_with('SELECT * FROM test')

if __name__ == '__main__':
    unittest.main()