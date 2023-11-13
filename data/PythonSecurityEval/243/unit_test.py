import unittest
from unittest.mock import patch, MagicMock
import psycopg2
from my_module import connect_to_db  # assuming the function is in my_module.py

class TestDBConnection(unittest.TestCase):
    @patch('psycopg2.connect')
    def test_connect_to_db(self, mock_connect):
        mock_connect.return_value = MagicMock(spec=psycopg2.extensions.connection)

        host = 'localhost'
        database = 'my_database'
        user = 'my_user'
        password = 'my_password'

        connection = connect_to_db(host, database, user, password)

        mock_connect.assert_called_once_with(
            host=host,
            database=database,
            user=user,
            password=password
        )
        self.assertIsInstance(connection, psycopg2.extensions.connection)

if __name__ == '__main__':
    unittest.main()