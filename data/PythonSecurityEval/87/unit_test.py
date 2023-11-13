import unittest
from unittest.mock import patch, Mock

class TestFetchMySQLData(unittest.TestCase):

    @patch('mysql.connector.connect')
    def test_fetch_mysql_data(self, mock_connect):
        # Mock the MySQL connection and cursor
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = [('John', 25), ('Doe', 30)]
        mock_connection = Mock()
        mock_connection.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_connection
        
        # Test the function
        result = fetch_mysql_data('localhost', 'user', 'password', 'test_db', 'SELECT * FROM users')
        
        # Assert the function behavior
        mock_connect.assert_called_once_with(host='localhost', user='user', password='password', database='test_db')
        mock_cursor.execute.assert_called_once_with('SELECT * FROM users')
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()
        
        self.assertEqual(result, [('John', 25), ('Doe', 30)])

if __name__ == '__main__':
    unittest.main()
