import unittest
from unittest.mock import patch, Mock
import mysql.connector
from your_module import create_user  # replace 'your_module' with the name of your module

class TestCreateUser(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_create_user(self, mock_connect):
        # Create a mock cursor object
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Test the create_user function
        result = create_user('testuser', 'testpassword')

        # Assert that the connect method was called once
        self.assertEqual(mock_connect.call_count, 1)

        # Assert that the cursor method was called once
        self.assertEqual(mock_connect.return_value.cursor.call_count, 1)

        # Assert that the execute method was called once with the correct SQL query
        mock_cursor.execute.assert_called_once_with("CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testpassword';")

        # Assert that the commit method was called once
        self.assertEqual(mock_connect.return_value.commit.call_count, 1)

        # Assert that the close method was called twice (once for the cursor and once for the connection)
        self.assertEqual(mock_connect.return_value.close.call_count, 2)

        # Assert that the function returned True
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()