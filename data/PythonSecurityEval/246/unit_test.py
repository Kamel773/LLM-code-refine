import unittest
from unittest.mock import mock_open, patch
import json

class TestParseJsonFile(unittest.TestCase):
    @patch('json.load')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
    def test_parse_json_file(self, mock_file, mock_json):
        mock_json.return_value = {"key": "value"}
        result = parse_json_file('dummy_file_path')
        self.assertEqual(result, {"key": "value"})
        mock_file.assert_called_once_with('dummy_file_path', 'r')
        mock_json.assert_called_once_with(mock_file.return_value)

if __name__ == '__main__':
    unittest.main()