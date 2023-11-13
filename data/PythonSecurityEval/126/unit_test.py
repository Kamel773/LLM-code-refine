import unittest
from unittest.mock import patch, Mock
import requests
import json

class TestReadJsonFromUrl(unittest.TestCase):
    @patch('requests.get')
    def test_read_json_from_url(self, mock_get):
        mock_response = Mock()
        expected_dict = {"key": "value"}
        mock_response.text = json.dumps(expected_dict)
        mock_get.return_value = mock_response

        url = 'http://example.com'
        result = read_json_from_url(url)

        self.assertEqual(result, expected_dict)
        mock_get.assert_called_once_with(url)

if __name__ == '__main__':
    unittest.main()