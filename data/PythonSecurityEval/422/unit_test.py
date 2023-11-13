import unittest
from unittest.mock import patch, Mock
import pyodbc

class TestDatabase(unittest.TestCase):
    @patch('pyodbc.connect')
    def test_execute_sql_query(self, mock_connect):
        # Arrange
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        connection_string = "Driver={SQL Server};Server=server_name;Database=db_name;Trusted_Connection=yes;"
        query = "SELECT * FROM table_name"

        # Act
        result = execute_sql_query(connection_string, query)

        # Assert
        mock_connect.assert_called_once_with(connection_string)
        mock_cursor.execute.assert_called_once_with(query)
        mock_connect.return_value.commit.assert_called_once()
        mock_connect.return_value.close.assert_called_once()
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()