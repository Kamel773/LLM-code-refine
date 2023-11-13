import unittest
from unittest.mock import patch, MagicMock

class TestVacuumDB(unittest.TestCase):
    @patch('psycopg2.connect')
    def test_vacuum_db(self, mock_connect):
        # Create a mock connection, cursor and assign to the return_value of the mock_connect
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur

        # Call the function we're testing
        vacuum_db('localhost', 'test_db', 'user', 'password')

        # Assert that the mock connection and cursor were used as expected
        mock_connect.assert_called_once_with(dbname='test_db', user='user', password='password', host='localhost')
        mock_conn.autocommit = True
        mock_cur.execute.assert_called_once_with("VACUUM")
        mock_cur.close.assert_called_once()
        mock_conn.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()
