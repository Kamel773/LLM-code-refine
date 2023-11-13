import unittest
from unittest.mock import patch, Mock
import mysql.connector
import your_module  # replace with the name of your module

class TestDatabaseConnection(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_connect_to_database(self, mock_connect):
        mock_connect.return_value = Mock(spec=mysql.connector.MySQLConnection)

        result = your_module.connect_to_database()

        self.assertIsInstance(result, mysql.connector.MySQLConnection)
        mock_connect.assert_called_once_with(
            host="localhost",
            user="root",
            password=""
        )

if __name__ == "__main__":
    unittest.main()