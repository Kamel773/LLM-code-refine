import unittest
from unittest.mock import patch, mock_open
import my_module  # replace with the name of the module where download_file is defined

class TestDownloadFile(unittest.TestCase):
    @patch('my_module.requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_download_file(self, mock_open, mock_get):
        mock_response = mock_get.return_value
        mock_response.content = b'file content'

        my_module.download_file('http://example.com', 'example.txt')

        mock_get.assert_called_once_with('http://example.com')
        mock_open.assert_called_once_with('example.txt', 'wb')
        handle = mock_open()
        handle.write.assert_called_once_with(b'file content')

if __name__ == '__main__':
    unittest.main()