import unittest
from unittest.mock import patch, Mock
import requests

class TestSendRequest(unittest.TestCase):
    @patch('requests.get')
    def test_send_request(self, mock_get):
        # Mock the response returned by requests.get
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = 'Success'
        mock_get.return_value = mock_response

        # Call the function with the mocked requests.get
        response = send_request('http://fakeurl.com')

        # Assert the function made the expected calls and returned the correct result
        mock_get.assert_called_once_with('http://fakeurl.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Success')

if __name__ == '__main__':
    unittest.main()