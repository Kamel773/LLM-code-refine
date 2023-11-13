import unittest
from unittest.mock import patch, MagicMock
import pymysql
from my_module import connect_to_database  # assuming the function is in a module named my_module

class TestDatabaseConnection(unittest.TestCase):
    @patch('pymysql.connect')
    def test_connect_to_database(self, mock_connect):
        mock_connect.return_value = MagicMock()
        
        result = connect_to_database('localhost', 'user', 'password', 'db')
        
        self.assertIsNotNone(result)
        mock_connect.assert_called_once_with(host='localhost', user='user', password='password', db='db')

if __name__ == '__main__':
    unittest.main()