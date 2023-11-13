import unittest
from unittest.mock import patch, mock_open
import os

class TestStoreBinaryFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data=b'test data')
    @patch('sqlite3.connect')
    @patch('os.path.isfile', return_value=True)
    def test_store_binary_file(self, mock_isfile, mock_sqlite3, mock_file):
        from store_binary_file import store_binary_file  # Assuming the function is in this module

        # Call the function
        store_binary_file('test_file')

        # Assert file was read
        mock_file.assert_called_once_with('test_file', 'rb')

        # Assert database connection was established
        mock_sqlite3.assert_called_once_with('binary_db.sqlite')

        # Assert execute calls
        mock_sqlite3.return_value.execute.assert_any_call('''CREATE TABLE IF NOT EXISTS binary_table
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, data BLOB NOT NULL);''')
        mock_sqlite3.return_value.execute.assert_any_call('''INSERT INTO binary_table (data) VALUES (?);''', (sqlite3.Binary(b'test data'),))

        # Assert commit was called
        mock_sqlite3.return_value.commit.assert_called_once()

        # Assert connection was closed
        mock_sqlite3.return_value.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()