import unittest
from unittest.mock import mock_open, patch
import csv_module  # assuming the above functions are in a module named csv_module

class TestCsvModule(unittest.TestCase):
    @patch('csv_module.csv.writer')
    @patch('builtins.open', new_callable=mock_open)
    def test_write_to_csv(self, mock_file, mock_csv):
        data = [['Name', 'Age'], ['John', '23'], ['Doe', '24']]
        csv_module.write_to_csv('test.csv', data)
        mock_file.assert_called_once_with('test.csv', mode='w', newline='')
        mock_csv().writerows.assert_called_once_with(data)

    @patch('csv_module.csv.reader')
    @patch('builtins.open', new_callable=mock_open)
    def test_read_from_csv(self, mock_file, mock_csv):
        mock_csv.return_value = iter([['Name', 'Age'], ['John', '23'], ['Doe', '24']])
        result = csv_module.read_from_csv('test.csv')
        mock_file.assert_called_once_with('test.csv', mode='r')
        self.assertEqual(result, [['Name', 'Age'], ['John', '23'], ['Doe', '24']])

if __name__ == '__main__':
    unittest.main()