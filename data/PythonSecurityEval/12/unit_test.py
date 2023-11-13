import unittest
from unittest.mock import patch, Mock
import pandas as pd

class TestLoadCSVToSQLite(unittest.TestCase):
    @patch('pandas.read_csv')
    @patch('sqlite3.connect')
    def test_load_csv_to_sqlite(self, mock_sqlite3_connect, mock_read_csv):
        mock_conn = Mock()
        mock_sqlite3_connect.return_value = mock_conn
        mock_df = Mock()
        mock_read_csv.return_value = mock_df

        load_csv_to_sqlite('test.csv', 'test_table', 'test.db')

        mock_read_csv.assert_called_once_with('test.csv')
        mock_df.to_sql.assert_called_once_with('test_table', mock_conn, if_exists='replace', index=False)
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()