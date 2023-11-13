import unittest
from unittest.mock import mock_open, patch
from my_module import extract_data_from_json  # assuming the function is in a file named my_module.py

class TestExtractDataFromJson(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
    def test_extract_data_from_json(self, mock_file):
        expected_data = {"key": "value"}
        actual_data = extract_data_from_json('dummy_path')
        self.assertEqual(actual_data, expected_data)

    @patch('builtins.open', new_callable=mock_open, read_data='not a json string')
    def test_extract_data_from_json_invalid_json(self, mock_file):
        actual_data = extract_data_from_json('dummy_path')
        self.assertIsNone(actual_data)

    @patch('builtins.open', side_effect=FileNotFoundError())
    def test_extract_data_from_json_file_not_found(self, mock_file):
        actual_data = extract_data_from_json('dummy_path')
        self.assertIsNone(actual_data)

if __name__ == '__main__':
    unittest.main()