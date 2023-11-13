import unittest
from unittest.mock import patch, Mock
import pyodbc

class TestDBConnection(unittest.TestCase):

    @patch('pyodbc.connect')
    def test_connection_success(self, mock_connect):
        mock_connect.return_value = Mock()
        server = 'test_server'
        database = 'test_db'
        username = 'test_user'
        password = 'test_pass'

        conn = connect_to_sql_server(server, database, username, password)

        mock_connect.assert_called_once_with('DRIVER={ODBC Driver 17 for SQL Server};'
                                             f'SERVER={server};'
                                             f'DATABASE={database};'
                                             f'UID={username};'
                                             f'PWD={password}')
        self.assertIsNotNone(conn)
    
    @patch('pyodbc.connect')
    def test_connection_exception(self, mock_connect):
        mock_connect.side_effect = pyodbc.Error('Failed to connect')
        server = 'test_server'
        database = 'test_db'
        username = 'test_user'
        password = 'test_pass'

        with self.assertRaises(pyodbc.Error):
            connect_to_sql_server(server, database, username, password)

        mock_connect.assert_called_once_with('DRIVER={ODBC Driver 17 for SQL Server};'
                                             f'SERVER={server};'
                                             f'DATABASE={database};'
                                             f'UID={username};'
                                             f'PWD={password}')

if __name__ == '__main__':
    unittest.main()
