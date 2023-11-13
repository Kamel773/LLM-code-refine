import unittest
from unittest.mock import patch, Mock
import sqlite3

class TestDatabaseFunctions(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE my_table (id integer, value text)")

    def tearDown(self):
        self.conn.close()

    @patch('sqlite3.connect')
    def test_insert_array_to_db(self, mock_connect):
        mock_connect.return_value = Mock()
        mock_connect.return_value.cursor.return_value = self.cursor

        test_array = ['test1', 'test2', 'test3']
        insert_array_to_db(test_array)

        self.cursor.execute("SELECT * FROM my_table")
        rows = self.cursor.fetchall()

        self.assertEqual(len(rows), len(test_array))
        for i, row in enumerate(rows):
            self.assertEqual(row[0], i)
            self.assertEqual(row[1], test_array[i])

if __name__ == '__main__':
    unittest.main()