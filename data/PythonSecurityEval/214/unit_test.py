import unittest
from unittest.mock import patch, Mock
import mysql.connector
from my_module import create_table  # assuming the function is in my_module.py

class TestCreateTable(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_create_table(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        db_config = {'user': 'root', 'password': 'password', 'host': 'localhost', 'database': 'test_db'}
        table_name = 'test_table'
        create_table(db_config, table_name)

        mock_connect.assert_called_once_with(**db_config)
        mock_cursor.execute.assert_called_once_with(f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
        mock_cursor.close.assert_called_once()
        mock_connect.return_value.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()