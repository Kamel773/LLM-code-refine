import unittest
from unittest.mock import patch
import requests

class TestPostRequest(unittest.TestCase):
    @patch('requests.post')
    def test_send_post_request(self, mock_post):
        url = 'http://example.com'
        data = {'key': 'value'}
        mock_response = mock_post.return_value
        mock_response.status_code = 200

        response = send_post_request(url, data)

        mock_post.assert_called_once_with(url, data=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()