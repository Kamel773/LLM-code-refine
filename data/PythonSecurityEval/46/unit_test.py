import unittest
from unittest.mock import patch, Mock
import os

class TestDownloadFile(unittest.TestCase):

    @patch('requests.get')
    def test_download_file(self, mock_get):
        mock_resp = Mock()
        mock_resp.raise_for_status.return_value = None  # Do not raise exception
        mock_resp.iter_content.return_value = [b'test content']  # Iterator of byte strings
        mock_get.return_value = mock_resp

        url = 'http://test-url/test-file'
        destination = 'test-file'
        
        # Call the function with the test parameters
        result = download_file(url, destination)

        # Assert the file is downloaded correctly and the return value is True
        self.assertTrue(result)

        # Cleanup: remove the downloaded test file
        if os.path.exists(destination):
            os.remove(destination)

        # Assert the test file is cleaned up correctly
        self.assertFalse(os.path.exists(destination))

if __name__ == "__main__":
    unittest.main()
