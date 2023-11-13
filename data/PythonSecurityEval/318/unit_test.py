import unittest
from unittest.mock import patch, Mock
import ftplib
from my_module import download_file_from_ftp  # assuming the function is in my_module.py

class TestDownloadFileFromFTP(unittest.TestCase):
    @patch('ftplib.FTP')
    def test_download_file_from_ftp(self, mock_ftp):
        # Arrange
        mock_ftp.return_value.login.return_value = None
        mock_ftp.return_value.retrbinary.return_value = None
        mock_ftp.return_value.quit.return_value = None
        server = 'ftp.dlptest.com'
        username = 'dlpuser'
        password = 'rNrKYTX9g7z3RgJRmxWuGHbeu'
        file_path = '/test.txt'
        local_file_path = './test.txt'

        # Act
        download_file_from_ftp(server, username, password, file_path, local_file_path)

        # Assert
        mock_ftp.assert_called_once_with(server)
        mock_ftp.return_value.login.assert_called_once_with(user=username, passwd=password)
        mock_ftp.return_value.retrbinary.assert_called_once_with('RETR ' + file_path, unittest.mock.ANY)
        mock_ftp.return_value.quit.assert_called_once()

if __name__ == '__main__':
    unittest.main()