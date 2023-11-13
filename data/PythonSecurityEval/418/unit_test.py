import unittest
from unittest.mock import patch, MagicMock
from my_module import connect_to_ftp  # assuming the function is in my_module.py

class TestFTPConnection(unittest.TestCase):
    @patch('my_module.FTP')
    def test_connect_to_ftp(self, mock_ftp):
        # Arrange
        mock_ftp_instance = MagicMock()
        mock_ftp.return_value = mock_ftp_instance
        server = 'ftp.dlptest.com'
        username = 'dlpuser'
        password = 'rNrKYTX9g7z3RgJRmxWuGHbeu'

        # Act
        result = connect_to_ftp(server, username, password)

        # Assert
        mock_ftp.assert_called_once_with(server)
        mock_ftp_instance.login.assert_called_once_with(user=username, passwd=password)
        self.assertEqual(result, mock_ftp_instance)

if __name__ == '__main__':
    unittest.main()