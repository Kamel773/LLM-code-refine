import unittest
from unittest.mock import patch, Mock
from urllib.parse import urlparse

class TestGetFilenameFromUrl(unittest.TestCase):
    @patch('os.path.basename')
    @patch('urllib.parse.urlparse')
    def test_get_filename_from_url(self, mock_urlparse, mock_basename):
        mock_url = 'http://example.com/path/to/file.txt'
        mock_urlparse.return_value = urlparse(mock_url)
        mock_basename.return_value = 'file.txt'

        result = get_filename_from_url(mock_url)

        mock_urlparse.assert_called_once_with(mock_url)
        mock_basename.assert_called_once_with(mock_urlparse(mock_url).path)
        self.assertEqual(result, 'file.txt')

if __name__ == '__main__':
    unittest.main()