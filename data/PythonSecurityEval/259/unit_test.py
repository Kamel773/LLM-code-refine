import unittest
from unittest.mock import patch, Mock
import psycopg2
from psycopg2 import sql
import your_module  # replace with the name of the module where you defined the above function

class TestCreateUser(unittest.TestCase):
    @patch('psycopg2.connect')
    def test_create_user(self, mock_connect):
        mock_conn = mock_connect.return_value
        mock_cur = mock_conn.cursor.return_value

        your_module.create_user('testuser', 'testpassword')  # replace 'your_module' with the name of your module

        mock_connect.assert_called_once_with(dbname='mydatabase', user='postgres', password='postgres', host='localhost', port='5432')
        mock_conn.cursor.assert_called_once()
        mock_cur.execute.assert_called_once_with(sql.SQL("CREATE USER {} WITH PASSWORD '{}';").format(
            sql.Identifier('testuser'),
            sql.SQL('testpassword')))
        mock_cur.close.assert_called_once()
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()