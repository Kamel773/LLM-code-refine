import unittest
from unittest.mock import patch, Mock

class TestFTPUpload(unittest.TestCase):

    @patch('ftplib.FTP')  # corrected target for patching
    def test_upload_file_ftp(self, mock_ftp):
        # Setup
        mock_ftp_instance = Mock()
        mock_ftp.return_value = mock_ftp_instance

        # Call the function
        result = upload_file_ftp('localhost', 'user', 'pass', '/path/to/file')  # replace with your actual module name

        # Assert that the function behaved as expected
        self.assertTrue(result)
        mock_ftp.assert_called_with('localhost')
        mock_ftp_instance.login.assert_called_with('user', 'pass')
        mock_ftp_instance.storbinary.assert_called()
        mock_ftp_instance.quit.assert_called()

if __name__ == '__main__':
    unittest.main()
