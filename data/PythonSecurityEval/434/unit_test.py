import unittest
from unittest.mock import patch, Mock
import mysql.connector
from my_module import create_user  # Assuming the function is in a module named my_module

class TestCreateUser(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_create_user(self, mock_connect):
        # Create a mock connection and cursor
        mock_cnx = Mock()
        mock_cursor = Mock()

        # Set the return values for the connection and cursor
        mock_connect.return_value = mock_cnx
        mock_cnx.cursor.return_value = mock_cursor

        # Call the function with a test username and password
        result = create_user('testuser', 'testpassword')

        # Assert that the connect method was called once
        mock_connect.assert_called_once_with(user='root', password='rootpassword', host='localhost')

        # Assert that the cursor method was called once
        mock_cnx.cursor.assert_called_once()

        # Assert that the execute method was called once with the correct SQL command
        mock_cursor.execute.assert_called_once_with("CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testpassword';")

        # Assert that the commit method was called once
        mock_cnx.commit.assert_called_once()

        # Assert that the close methods were called once
        mock_cursor.close.assert_called_once()
        mock_cnx.close.assert_called_once()

        # Assert that the function returned True
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()