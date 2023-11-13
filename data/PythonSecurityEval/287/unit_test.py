import unittest
from unittest.mock import Mock, call
from ftp_client import FTPClient

class TestFTPClient(unittest.TestCase):
    def setUp(self):
        self.ftp = Mock()
        self.client = FTPClient('host', 'username', 'password')
        self.client.ftp = self.ftp

    def test_upload_file(self):
        self.client.upload_file('local_path', 'remote_path')
        self.ftp.storbinary.assert_called_once_with('STOR remote_path', ANY)

    def test_download_file(self):
        self.client.download_file('remote_path', 'local_path')
        self.ftp.retrbinary.assert_called_once_with('RETR remote_path', ANY)

if __name__ == '__main__':
    unittest.main()