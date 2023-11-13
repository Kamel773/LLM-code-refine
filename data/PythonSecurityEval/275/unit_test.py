import unittest
from unittest.mock import mock_open, patch
import csv

class TestCsvToDict(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='name,age\nJohn,23\nJane,25')
    def test_csv_to_dict(self, mock_file):
        expected_result = [{'name': 'John', 'age': '23'}, {'name': 'Jane', 'age': '25'}]
        result = csv_to_dict('test.csv')
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()