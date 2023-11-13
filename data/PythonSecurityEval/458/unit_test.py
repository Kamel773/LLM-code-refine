import unittest
from unittest.mock import patch, Mock
import download_file_module  # replace with the name of the module where you defined the download_file function

class TestDownloadFile(unittest.TestCase):
    @patch('requests.get')
    def test_download_file(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.iter_content = lambda chunk_size: [b'chunk1', b'chunk2', b'chunk3']
        mock_get.return_value = mock_response

        download_file_module.download_file('http://example.com', 'path/to/save')

        mock_get.assert_called_once_with('http://example.com', stream=True)
        with open('path/to/save', 'rb') as file:
            content = file.read()
        self.assertEqual(content, b'chunk1chunk2chunk3')

if __name__ == '__main__':
    unittest.main()