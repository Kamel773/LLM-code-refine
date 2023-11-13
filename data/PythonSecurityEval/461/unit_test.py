import unittest
from unittest.mock import patch, mock_open
import your_module  # replace with the name of the module where parse_json is defined

class TestParseJson(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
    def test_parse_json(self, mock_file):
        result = your_module.parse_json('{"key": "value"}')
        self.assertEqual(result, {"key": "value"})

    @patch("builtins.open", new_callable=mock_open, read_data='not a json string')
    def test_parse_json_invalid(self, mock_file):
        result = your_module.parse_json('not a json string')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()