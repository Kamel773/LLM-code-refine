import unittest
from unittest.mock import patch
import requests

class TestGetRequestNoSSL(unittest.TestCase):
    @patch('requests.get')
    def test_get_request_no_ssl(self, mock_get):
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = b'OK'
        mock_get.return_value = mock_response

        response = get_request_no_ssl('https://www.example.com')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'OK')

if __name__ == '__main__':
    unittest.main()