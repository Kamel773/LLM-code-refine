import unittest
from unittest.mock import patch, mock_open
import your_module  # replace with the name of the module where you defined the function

class TestStoreDataInDb(unittest.TestCase):
    @patch('your_module.psycopg2.connect')
    @patch('builtins.open', new_callable=mock_open, read_data='id,name,email\n1,John,john@example.com\n')
    def test_store_data_in_db(self, mock_file, mock_db):
        mock_cursor = mock_db.return_value.cursor.return_value
        your_module.store_data_in_db('dummy.csv', {'dbname': 'test', 'user': 'test', 'password': 'test', 'host': 'localhost'})
        mock_file.assert_called_once_with('dummy.csv', 'r')
        mock_db.assert_called_once_with(dbname='test', user='test', password='test', host='localhost')
        mock_cursor.execute.assert_called_once_with("INSERT INTO your_table VALUES (%s, %s, %s)", ['1', 'John', 'john@example.com'])

if __name__ == '__main__':
    unittest.main()