import unittest
from unittest.mock import patch, Mock
import requests

class TestSendGetRequest(unittest.TestCase):
    @patch('requests.get')
    def test_send_get_request_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = 'Success'
        mock_get.return_value = mock_response

        response = send_get_request('http://example.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Success')

    @patch('requests.get')
    def test_send_get_request_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException('Error')

        response = send_get_request('http://example.com')
        self.assertEqual(response, 'Error')

if __name__ == '__main__':
    unittest.main()