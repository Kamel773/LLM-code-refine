import unittest
from unittest.mock import patch, MagicMock

class TestExecuteSqlQuery(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_execute_sql_query(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        db_name = 'test.db'
        query = 'SELECT * FROM test_table'

        execute_sql_query(db_name, query)

        mock_connect.assert_called_once_with(db_name)
        mock_conn.cursor().execute.assert_called_once_with(query)
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()