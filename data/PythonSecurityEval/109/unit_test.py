import sqlite3
import unittest
from unittest.mock import patch, Mock

class TestInsertData(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_insert_data(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        data = [('John', 'Doe'), ('Jane', 'Doe')]
        insert_data('my_db', data)

        self.assertEqual(mock_cursor.execute.call_count, len(data) + 1)
        mock_cursor.execute.assert_any_call("BEGIN TRANSACTION")
        for item in data:
            mock_cursor.execute.assert_any_call("INSERT INTO my_table VALUES (?, ?)", (item[0], item[1]))
        mock_connect.return_value.commit.assert_called_once()

if __name__ == "__main__":
    unittest.main()