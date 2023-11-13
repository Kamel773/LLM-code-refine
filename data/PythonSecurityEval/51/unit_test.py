import unittest
from unittest.mock import Mock, mock_open, call
from ftplib import FTP

class TestUploadDirectory(unittest.TestCase):
    def setUp(self):
        self.ftp = Mock(spec=FTP)
        self.ftp.storbinary = Mock()
        self.ftp.mkd = Mock()
        self.ftp.cwd = Mock()
        self.filename = "testfile"
        self.file_content = b"test file content"

    def test_upload_directory_with_single_file(self):
        with unittest.mock.patch('builtins.open', mock_open(read_data=self.file_content)), unittest.mock.patch('os.listdir', return_value=[self.filename]), unittest.mock.patch('os.path.isfile', return_value=True), unittest.mock.patch('os.path.isdir', return_value=False):
            upload_directory(self.ftp, '/test')

        self.ftp.storbinary.assert_called_once_with(f'STOR {self.filename}', unittest.mock.ANY)
        self.ftp.mkd.assert_not_called()
        self.ftp.cwd.assert_not_called()

    def test_upload_directory_with_single_directory(self):
        with unittest.mock.patch('os.listdir', return_value=[self.filename]), unittest.mock.patch('os.path.isfile', return_value=False), unittest.mock.patch('os.path.isdir', return_value=True), unittest.mock.patch('os.listdir', return_value=[]):
            upload_directory(self.ftp, '/test')

        self.ftp.mkd.assert_called_once_with(self.filename)
        self.ftp.cwd.assert_has_calls([call(self.filename), call('..')])
        self.ftp.storbinary.assert_not_called()

if __name__ == '__main__':
    unittest.main()
