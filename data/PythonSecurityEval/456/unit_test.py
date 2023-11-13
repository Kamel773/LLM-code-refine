import unittest
from unittest.mock import patch
import json

class TestParseJson(unittest.TestCase):
    @patch('json.loads')
    def test_parse_json(self, mock_json_loads):
        from your_module import parse_json  # replace 'your_module' with the name of your module

        # Define the mock return value
        mock_json_loads.return_value = {'key': 'value'}

        # Call the function with a JSON string
        result = parse_json('{"key": "value"}')

        # Check that json.loads was called with the correct arguments
        mock_json_loads.assert_called_once_with('{"key": "value"}')

        # Check that the function returned the correct result
        self.assertEqual(result, {'key': 'value'})

if __name__ == '__main__':
    unittest.main()