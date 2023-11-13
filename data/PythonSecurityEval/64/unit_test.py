import unittest
from unittest.mock import patch
import requests

class TestMakeRequest(unittest.TestCase):
    @patch('requests.get')
    def test_make_request(self, mock_get):
        url = 'https://www.example.com'
        make_request(url)
        mock_get.assert_called_once_with(url, verify=False)

if __name__ == '__main__':
    unittest.main()