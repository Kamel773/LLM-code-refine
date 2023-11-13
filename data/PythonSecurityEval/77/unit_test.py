import unittest
from unittest.mock import patch, Mock

class TestSqliteToDataframe(unittest.TestCase):
    
    @patch('sqlite3.connect')
    @patch('pandas.read_sql')
    def test_sqlite_to_dataframe(self, mock_read_sql, mock_connect):
        # Mocking the database connection and read_sql function
        mock_conn = Mock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_read_sql.return_value = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        
        # Test function
        db_path = 'mock_db_path'
        query = 'SELECT * FROM mock_table'
        df = sqlite_to_dataframe(db_path, query)
        
        # Assertions
        mock_connect.assert_called_once_with(db_path)
        mock_read_sql.assert_called_once_with(query, mock_conn)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(df.shape, (2, 2))

if __name__ == '__main__':
    unittest.main()