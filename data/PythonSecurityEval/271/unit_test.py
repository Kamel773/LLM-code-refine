import unittest
from unittest.mock import mock_open, patch
import json

class TestExtractDataFromJson(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps({"key": "value"}))
    def test_extract_data_from_json(self, mock_file):
        result = extract_data_from_json('fake_path')
        self.assertEqual(result, {"key": "value"})

if __name__ == '__main__':
    unittest.main()