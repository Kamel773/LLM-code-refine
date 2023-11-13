import unittest
from unittest.mock import patch, mock_open, MagicMock

class TestImportCSVToSqlite(unittest.TestCase):

    @patch('sqlite3.connect')
    @patch('csv.DictReader')
    @patch('builtins.open', new_callable=mock_open, read_data='col1,col2\nval1,val2\n')
    def test_import_csv_to_sqlite(self, mock_file, mock_csv, mock_sql):
        mock_csv.return_value.fieldnames = ['col1', 'col2']
        mock_csv.return_value.__iter__.return_value = [{'col1': 'val1', 'col2': 'val2'}]

        mock_conn = MagicMock()
        mock_sql.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor

        import_csv_to_sqlite('test.csv', 'test.db', 'test_table')

        mock_file.assert_called_once_with('test.csv', 'r')
        mock_csv.assert_called_once()
        mock_sql.assert_called_once_with('test.db')
        mock_cursor.execute.assert_any_call('DROP TABLE IF EXISTS test_table;')
        mock_cursor.execute.assert_any_call('CREATE TABLE test_table (col1, col2);')
        mock_cursor.executemany.assert_called_once_with('INSERT INTO test_table (col1, col2) VALUES (?, ?);', [('val1', 'val2')])
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
