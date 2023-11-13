import unittest
from unittest.mock import patch, Mock
from your_module import decode_auth_header  # replace 'your_module' with the name of your module

class TestDecodeAuthHeader(unittest.TestCase):
    @patch('your_module.request')  # replace 'your_module' with the name of your module
    def test_decode_auth_header(self, mock_request):
        # Mock the 'Authorization' header in the request
        mock_request.headers = {'Authorization': 'Basic dXNlcjpwYXNzd29yZA=='}

        # Call the function
        credentials = decode_auth_header()

        # Check the result
        self.assertEqual(credentials, 'user:password')

if __name__ == '__main__':
    unittest.main()