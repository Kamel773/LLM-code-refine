import unittest
from unittest.mock import patch, Mock
import mysql.connector
from my_module import connect_and_execute_query  # assuming the function is in my_module.py

class TestDatabaseConnection(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_connect_and_execute_query(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('test',)]

        result = connect_and_execute_query('localhost', 'user', 'password', 'database', 'SELECT * FROM table')

        mock_connect.assert_called_once_with(host='localhost', user='user', password='password', database='database')
        mock_cursor.execute.assert_called_once_with('SELECT * FROM table')
        self.assertEqual(result, [('test',)])

if __name__ == '__main__':
    unittest.main()