import unittest
from unittest.mock import patch, Mock
import mysql.connector
import your_module  # replace with the name of the module where execute_query is defined

class TestExecuteQuery(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_execute_query(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        your_module.execute_query('SELECT * FROM table')

        mock_connect.assert_called_once_with(user='username', password='password',
                                             host='localhost',
                                             database='database_name')
        mock_cursor.execute.assert_called_once_with('SELECT * FROM table')
        mock_connect.return_value.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()