import unittest
from unittest.mock import patch, call
import sqlite3

class TestCreateTable(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_create_table(self, mock_connect):
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        create_table('test.db', 'stocks', 'date text, trans text, symbol text, qty real, price real')

        mock_connect.assert_called_once_with('test.db')
        mock_cursor.execute.assert_called_once_with('CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)')
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()