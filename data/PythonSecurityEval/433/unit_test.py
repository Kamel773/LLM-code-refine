import unittest
from unittest.mock import patch, Mock
import mysql.connector
from mysql.connector import Error

class TestDBConnection(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_create_connection(self, mock_connect):
        mock_connect.return_value = Mock()
        result = create_connection("localhost", "root", "password", "test_db")
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()