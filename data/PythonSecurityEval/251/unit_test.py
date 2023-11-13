import unittest
from unittest.mock import patch, MagicMock
import your_module  # replace with the name of the module where `execute_query` is defined

class TestExecuteQuery(unittest.TestCase):
    @patch('psycopg2.connect')
    def test_execute_query(self, mock_connect):
        # Mock the connection and the cursor
        mock_conn = MagicMock()
        mock_cur = MagicMock()

        # Set the return values
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur
        mock_cur.fetchall.return_value = [('test',)]

        # Call the function with the mock
        result = your_module.execute_query('SELECT * FROM table')

        # Assert the function returns the correct result
        self.assertEqual(result, [('test',)])

        # Assert the function calls the mocks correctly
        mock_connect.assert_called_once_with(
            dbname="your_database",
            user="your_username",
            password="your_password",
            host="localhost",
            port="5432"
        )
        mock_conn.cursor.assert_called_once()
        mock_cur.execute.assert_called_once_with('SELECT * FROM table')
        mock_cur.fetchall.assert_called_once()

if __name__ == '__main__':
    unittest.main()