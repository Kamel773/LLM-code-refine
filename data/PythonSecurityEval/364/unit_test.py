import unittest
from unittest.mock import patch, Mock
import download_file

class TestDownloadFile(unittest.TestCase):
    @patch('requests.get')
    def test_download_file(self, mock_get):
        mock_response = Mock()
        mock_response.content = b'Test content'
        mock_get.return_value = mock_response

        download_file.download_file('http://testurl.com', 'testfile')

        mock_get.assert_called_once_with('http://testurl.com')
        with open('testfile', 'rb') as file:
            content = file.read()
        self.assertEqual(content, b'Test content')

if __name__ == '__main__':
    unittest.main()