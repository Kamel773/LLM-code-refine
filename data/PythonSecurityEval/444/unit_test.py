import unittest
from unittest.mock import patch, mock_open
from my_module import csv_to_dict  # assuming the function is in a file called my_module.py

class TestCsvToDict(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='name,age\nJohn,23\nDoe,45')
    def test_csv_to_dict(self, mock_file):
        expected_result = [{'name': 'John', 'age': '23'}, {'name': 'Doe', 'age': '45'}]
        self.assertEqual(csv_to_dict('any_file.csv'), expected_result)

if __name__ == '__main__':
    unittest.main()