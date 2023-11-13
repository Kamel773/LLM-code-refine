import unittest
from unittest.mock import patch, MagicMock
import psycopg2

class TestDatabaseConnection(unittest.TestCase):
    @patch('psycopg2.connect')
    def test_connect_to_db(self, mock_connect):
        mock_connect.return_value = MagicMock()

        credentials = {
            'dbname': 'test_db',
            'user': 'test_user',
            'password': 'test_password',
            'host': 'localhost',
            'port': '5432'
        }

        result = connect_to_db(credentials)

        self.assertIsNotNone(result)
        mock_connect.assert_called_once_with(
            dbname='test_db',
            user='test_user',
            password='test_password',
            host='localhost',
            port='5432'
        )

if __name__ == '__main__':
    unittest.main()