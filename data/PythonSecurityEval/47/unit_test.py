import unittest
from unittest.mock import patch
import io

class TestDownloadFile(unittest.TestCase):
    @patch('time.sleep')  # This patches the sleep function so the test runs instantly
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_download_file(self, mock_stdout, mock_sleep):
        download_file(10)
        output = mock_stdout.getvalue()
        self.assertTrue("Download progress: 100.00%" in output)
        self.assertTrue("Download completed." in output)

if __name__ == '__main__':
    unittest.main()
