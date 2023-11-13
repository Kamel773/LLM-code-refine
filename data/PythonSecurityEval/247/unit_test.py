import unittest
from unittest.mock import mock_open, patch
import csv_to_dict_module  # assuming the function above is in this module

class TestCsvToDict(unittest.TestCase):
    @patch('csv_to_dict_module.csv.DictReader')
    @patch('csv_to_dict_module.open', new_callable=mock_open, read_data='col1,col2\nval1,val2')
    def test_csv_to_dict(self, mock_open, mock_csv):
        mock_csv.return_value = [{'col1': 'val1', 'col2': 'val2'}]
        result = csv_to_dict_module.csv_to_dict('test.csv')
        self.assertEqual(result, [{'col1': 'val1', 'col2': 'val2'}])

if __name__ == '__main__':
    unittest.main()