import unittest
from unittest.mock import patch, Mock
import mysql.connector
from your_module import create_connection  # replace 'your_module' with the name of the module where you defined the create_connection function

class TestCreateConnection(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_create_connection(self, mock_connect):
        mock_connect.return_value = Mock()
        
        result = create_connection('localhost', 'user', 'password', 'db')
        
        mock_connect.assert_called_once_with(host='localhost', user='user', passwd='password', database='db')
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()