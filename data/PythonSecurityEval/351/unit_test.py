import unittest
from unittest.mock import mock_open, patch
from my_module import load_csv_file  # assuming the function is in a file called my_module.py

class TestLoadCSVFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='a,b,c\n1,2,3\n4,5,6')
    def test_load_csv_file(self, mock_file):
        expected_data = [['a', 'b', 'c'], ['1', '2', '3'], ['4', '5', '6']]
        actual_data = load_csv_file('fake_path')
        self.assertEqual(actual_data, expected_data)

if __name__ == '__main__':
    unittest.main()