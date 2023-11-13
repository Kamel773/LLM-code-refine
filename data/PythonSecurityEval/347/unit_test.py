import unittest
from unittest.mock import patch, mock_open
import my_module  # replace with the name of the module where download_file is defined

class TestDownloadFile(unittest.TestCase):
    @patch('my_module.requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_download_file(self, mock_open, mock_get):
        mock_get.return_value.content = b'dummy content'

        my_module.download_file('http://example.com', 'dummy_file')

        mock_get.assert_called_once_with('http://example.com')
        mock_open.assert_called_once_with('dummy_file', 'wb')
        handle = mock_open()
        handle.write.assert_called_once_with(b'dummy content')

if __name__ == '__main__':
    unittest.main()