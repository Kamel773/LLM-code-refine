import unittest
from unittest.mock import patch, Mock

class TestInsertData(unittest.TestCase):

    @patch('MySQLdb.connect')
    def test_insert_data(self, mock_connect):
        # Mocking the connection and cursor
        mock_cursor = Mock()
        mock_connection = Mock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Call the function
        insert_data('localhost', 'user', 'password', 'test_db', 'test_table', 'John', 25)

        # Assert that the connection was made with the correct parameters
        mock_connect.assert_called_once_with(host='localhost', user='user', passwd='password', db='test_db')

        # Assert that the cursor executed the correct query with the correct parameters
        mock_cursor.execute.assert_called_once_with("INSERT INTO test_table (name, age) VALUES (%s, %s)", ('John', 25))

        # Assert that the commit was called
        mock_connection.commit.assert_called_once()

        # Assert that the cursor and connection were closed
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
