import unittest
from unittest.mock import patch, mock_open
import json

class TestReadJsonFile(unittest.TestCase):
    @patch('json.load')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
    def test_read_json_file(self, mock_file, mock_json):
        mock_json.return_value = {"key": "value"}
        result = read_json_file('test.json')
        self.assertEqual(result, {"key": "value"})
        mock_file.assert_called_once_with('test.json', 'r')
        mock_json.assert_called_once()

if __name__ == '__main__':
    unittest.main()