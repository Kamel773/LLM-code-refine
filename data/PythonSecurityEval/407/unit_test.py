import unittest
from unittest.mock import patch, mock_open
import my_module  # replace with the name of the module where download_file is defined

class TestDownloadFile(unittest.TestCase):
    @patch('my_module.requests.get')
    def test_download_file(self, mock_get):
        mock_get.return_value.content = b'some file content'
        mock_file = mock_open()
        with patch('my_module.open', mock_file):
            my_module.download_file('http://example.com', 'local_file.txt')
        mock_file().write.assert_called_once_with(b'some file content')

if __name__ == '__main__':
    unittest.main()