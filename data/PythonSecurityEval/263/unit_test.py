import unittest
from unittest.mock import patch, Mock
import my_module  # replace with the name of the module where send_post_request is defined

class TestSendPostRequest(unittest.TestCase):
    @patch('requests.post')
    def test_send_post_request(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'success': True}
        mock_post.return_value = mock_response

        url = 'http://example.com'
        payload = {'key': 'value'}
        response = my_module.send_post_request(url, payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'success': True})
        mock_post.assert_called_once_with(url, data='{"key": "value"}', headers={'Content-Type': 'application/json'})

if __name__ == '__main__':
    unittest.main()