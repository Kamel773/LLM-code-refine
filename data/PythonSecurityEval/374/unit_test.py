import unittest
from unittest.mock import patch, Mock
import psycopg2

class TestExecuteQuery(unittest.TestCase):
    @patch('psycopg2.connect')
    def test_execute_query(self, mock_connect):
        # Arrange
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        query = "SELECT * FROM my_table"
        connection_params = {
            "dbname": "my_database",
            "user": "my_username",
            "password": "my_password",
            "host": "localhost",
            "port": "5432"
        }

        # Act
        result = execute_query(query, connection_params)

        # Assert
        mock_connect.assert_called_once_with(**connection_params)
        mock_cursor.execute.assert_called_once_with(query)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()