import unittest
from unittest.mock import patch, Mock
import mysql.connector

class TestInsertData(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_insert_data(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        insert_data('John', 25)

        mock_cursor.execute.assert_called_once_with("INSERT INTO customers (name, age) VALUES ('John', '25')")
        mock_connect.return_value.commit.assert_called_once()
        self.assertEqual(mock_cursor.rowcount, "record inserted.")

if __name__ == '__main__':
    unittest.main()