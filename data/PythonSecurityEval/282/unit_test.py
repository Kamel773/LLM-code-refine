import unittest
from unittest.mock import patch, mock_open
import mysql.connector
from mysql.connector import Error

class TestInsertDataFromCsvToDb(unittest.TestCase):
    @patch('mysql.connector.connect')
    @patch('builtins.open', new_callable=mock_open, read_data='id,name\n1,John\n2,Jane')
    def test_insert_data_from_csv_to_db(self, mock_file, mock_db):
        mock_cursor = mock_db.return_value.cursor.return_value
        mock_cursor.execute.side_effect = [None, None]  # Two rows in the CSV file

        insert_data_from_csv_to_db('test.csv', {}, 'test_table')

        # Check if the file was opened
        mock_file.assert_called_once_with('test.csv', 'r')

        # Check if the database connection was established
        mock_db.assert_called_once()

        # Check if the SQL statements were executed
        self.assertEqual(mock_cursor.execute.call_count, 2)

if __name__ == '__main__':
    unittest.main()