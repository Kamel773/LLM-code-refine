import unittest
from unittest.mock import patch, Mock
import mysql.connector
import your_module  # replace with the name of the module where you defined the above function

class TestDatabaseConnection(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_connect_to_database(self, mock_connect):
        mock_connect.return_value.is_connected.return_value = True

        result = your_module.connect_to_database('localhost', 'test_db', 'test_user', 'test_password')

        self.assertTrue(result.is_connected())
        mock_connect.assert_called_once_with(
            host='localhost',
            database='test_db',
            user='test_user',
            password='test_password'
        )

if __name__ == '__main__':
    unittest.main()