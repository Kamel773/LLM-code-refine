import unittest
from unittest.mock import patch, mock_open
import requests

class TestDownloadFile(unittest.TestCase):
    @patch('requests.get')
    def test_download_file(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.content = b'some file content'

        with patch('builtins.open', mock_open()) as mock_file:
            download_file('http://example.com', 'example.txt')

        mock_get.assert_called_once_with('http://example.com')
        mock_file().write.assert_called_once_with(b'some file content')

if __name__ == '__main__':
    unittest.main()