import unittest
from unittest.mock import patch, Mock
import MySQLdb
from my_module import connect_to_database  # assuming the function is in my_module.py

class TestDatabaseConnection(unittest.TestCase):
    @patch('MySQLdb.connect')
    def test_connect_to_database(self, mock_connect):
        mock_connect.return_value = Mock()
        
        # Test successful connection
        mock_connect.return_value = True
        response = connect_to_database('localhost', 'root', 'password', 'my_db')
        self.assertTrue(response)

        # Test failed connection
        mock_connect.side_effect = MySQLdb.Error('Failed to connect')
        response = connect_to_database('localhost', 'root', 'password', 'my_db')
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()