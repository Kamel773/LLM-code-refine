import unittest
from unittest.mock import mock_open, patch
import csv_module  # assuming the above functions are in csv_module.py

class TestCSVModule(unittest.TestCase):
    @patch('csv_module.csv.writer')
    @patch('builtins.open', new_callable=mock_open)
    def test_write_to_csv(self, mock_open_instance, mock_csv):
        data = [['Name', 'Age'], ['Alice', '23'], ['Bob', '25']]
        csv_module.write_to_csv('test.csv', data)
        mock_open_instance.assert_called_once_with('test.csv', 'w', newline='')
        mock_csv().writerows.assert_called_once_with(data)

    @patch('csv_module.csv.reader')
    @patch('builtins.open', new_callable=mock_open)
    def test_read_from_csv(self, mock_open_instance, mock_csv):
        data = [['Name', 'Age'], ['Alice', '23'], ['Bob', '25']]
        mock_csv.return_value = data
        result = csv_module.read_from_csv('test.csv')
        mock_open_instance.assert_called_once_with('test.csv', 'r')
        self.assertEqual(result, data)

if __name__ == '__main__':
    unittest.main()