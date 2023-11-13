import unittest
from unittest.mock import patch, Mock
import requests

class TestFetchJson(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_json(self, mock_get):
        mock_response = Mock()
        expected_dict = {"key": "value"}
        mock_response.json.return_value = expected_dict
        mock_get.return_value = mock_response

        url = 'http://example.com'
        result = fetch_json(url)

        self.assertEqual(result, expected_dict)
        mock_get.assert_called_once_with(url)
        mock_response.json.assert_called_once()

if __name__ == '__main__':
    unittest.main()