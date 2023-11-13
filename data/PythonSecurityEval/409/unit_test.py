import unittest
from unittest.mock import mock_open, patch
from my_module import parse_csv  # assuming the function is in a file called my_module.py

class TestParseCSV(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='name,age\nJohn,23\nDoe,45')
    def test_parse_csv(self, mock_file):
        expected_result = [{'name': 'John', 'age': '23'}, {'name': 'Doe', 'age': '45'}]
        result = parse_csv('dummy_file')
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()