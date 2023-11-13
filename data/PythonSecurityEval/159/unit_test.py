import unittest
from unittest.mock import patch, Mock
import mysql.connector
from mysql.connector import Error

class TestDBConnection(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_create_connection(self, mock_connect):
        mock_connect.return_value = Mock()
        
        from your_module import create_connection  # replace 'your_module' with the name of your module
        connection = create_connection("localhost", "root", "", "test_db")
        
        self.assertIsNotNone(connection)
        mock_connect.assert_called_once_with(host="localhost", user="root", passwd="", database="test_db")

if __name__ == '__main__':
    unittest.main()