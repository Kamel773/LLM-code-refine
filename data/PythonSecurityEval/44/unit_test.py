import unittest
from unittest.mock import patch, MagicMock

class TestGetFilenameFromUrl(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_get_filename_from_url(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.headers = {
            'Content-Disposition': 'attachment; filename="test_filename.txt"'
        }
        mock_urlopen.return_value = mock_response

        filename = get_filename_from_url('http://example.com/test_filename.txt')
        self.assertEqual(filename, 'test_filename.txt')

    @patch('urllib.request.urlopen')
    def test_get_filename_from_url_no_content_disposition(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.headers = {}
        mock_urlopen.return_value = mock_response

        filename = get_filename_from_url('http://example.com/test_filename.txt')
        self.assertEqual(filename, 'test_filename.txt')

if __name__ == '__main__':
    unittest.main()
