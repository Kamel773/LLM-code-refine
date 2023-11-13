import unittest
from unittest.mock import patch, MagicMock
from sqlalchemy import create_engine, text

class TestExecuteRawSqlQuery(unittest.TestCase):
    @patch('sqlalchemy.create_engine')
    def test_execute_raw_sql_query(self, mock_create_engine):
        mock_engine = MagicMock()
        mock_connection = MagicMock()
        mock_result = MagicMock()
        mock_create_engine.return_value = mock_engine
        mock_engine.connect.return_value.__enter__.return_value = mock_connection
        mock_connection.execute.return_value = mock_result
        mock_result.fetchall.return_value = [('test',)]

        database_uri = 'sqlite:///:memory:'
        query = 'SELECT * FROM test_table'
        result = execute_raw_sql_query(database_uri, query)

        mock_create_engine.assert_called_once_with(database_uri)
        mock_connection.execute.assert_called_once_with(text(query))
        mock_result.fetchall.assert_called_once()

        self.assertEqual(result, [('test',)])

if __name__ == '__main__':
    unittest.main()