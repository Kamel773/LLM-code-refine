import unittest
from unittest.mock import patch, mock_open
import mysql.connector
from mysql.connector import errorcode

class TestParseJsonToMysql(unittest.TestCase):
    @patch('mysql.connector.connect')
    @patch('builtins.open', new_callable=mock_open, read_data='[{"key1": "value1", "key2": "value2"}]')
    def test_parse_json_to_mysql(self, mock_file, mock_db):
        mock_cursor = mock_db.return_value.cursor.return_value
        mock_cursor.execute.side_effect = [None, None]

        parse_json_to_mysql('dummy.json', {'user': 'root', 'password': 'password', 'host': 'localhost', 'database': 'test'})

        self.assertTrue(mock_file.called)
        self.assertTrue(mock_db.called)
        self.assertTrue(mock_cursor.execute.called)

if __name__ == '__main__':
    unittest.main()