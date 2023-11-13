import unittest
from unittest.mock import patch
from requests.models import Response

class TestMakeRequestWithoutSSLVerification(unittest.TestCase):
    @patch('requests.get')
    def test_make_request_without_ssl_verification(self, mock_get):
        mock_response = Response()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = make_request_without_ssl_verification('https://example.com')

        self.assertEqual(response.status_code, 200)
        mock_get.assert_called_once_with('https://example.com', verify=False)

if __name__ == '__main__':
    unittest.main()