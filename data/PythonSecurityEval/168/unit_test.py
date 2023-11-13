import unittest
from unittest.mock import Mock, patch
from my_module import download_file  # assuming the function is in my_module.py

class TestDownloadFile(unittest.TestCase):
    @patch('my_module.FTP')
    def test_download_file(self, mock_ftp):
        # Set up the mock FTP object
        instance = mock_ftp.return_value
        instance.login.return_value = '230 Login successful.'
        instance.retrbinary.return_value = '226 Transfer complete.'

        # Call the function with mock data
        download_file('ftp.example.com', 'user', 'pass', 'file.txt')

        # Check that the methods were called with the correct arguments
        mock_ftp.assert_called_once_with('ftp.example.com')
        instance.login.assert_called_once_with(user='user', passwd='pass')
        instance.retrbinary.assert_called_once_with('RETR file.txt', ANY)
        instance.quit.assert_called_once()

if __name__ == '__main__':
    unittest.main()