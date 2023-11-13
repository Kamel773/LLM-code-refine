import unittest
from unittest.mock import patch, mock_open, MagicMock

class TestStoreDataInDb(unittest.TestCase):
    @patch('json.load')
    @patch('sqlite3.connect')
    def test_store_data_in_db(self, mock_connect, mock_load):
        # Mock data
        mock_load.return_value = [
            {'id': 1, 'name': 'Alice', 'age': 20},
            {'id': 2, 'name': 'Bob', 'age': 30}
        ]

        # Mock database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Call function
        store_data_in_db('data.json', 'data.db')

        # Check that methods were called with correct arguments
        mock_load.assert_called_once_with(mock_open().return_value.__enter__.return_value)
        mock_connect.assert_called_once_with('data.db')
        mock_cursor.execute.assert_any_call('''
            CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )
        ''')
        mock_cursor.execute.assert_any_call('''
            INSERT INTO data (id, name, age) VALUES (?, ?, ?)
        ''', (1, 'Alice', 20))
        mock_cursor.execute.assert_any_call('''
            INSERT INTO data (id, name, age) VALUES (?, ?, ?)
        ''', (2, 'Bob', 30))
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()