import unittest
from unittest.mock import patch, MagicMock
import os

class TestCreateUserDir(unittest.TestCase):
    @patch('os.getuid')
    @patch('os.setuid')
    @patch('pwd.getpwnam')
    @patch('os.path.exists')
    @patch('os.mkdir')
    @patch('os.chown')
    def test_create_user_dir(self, mock_chown, mock_mkdir, mock_exists, mock_getpwnam, mock_setuid, mock_getuid):
        mock_getuid.return_value = 1000
        mock_getpwnam.return_value = MagicMock(pw_uid=1000, pw_gid=1000)
        mock_exists.return_value = False

        create_user_dir('testuser')

        mock_setuid.assert_any_call(0)
        mock_getpwnam.assert_called_once_with('testuser')
        mock_exists.assert_called_once_with('/home/testuser')
        mock_mkdir.assert_called_once_with('/home/testuser')
        mock_chown.assert_called_once_with('/home/testuser', 1000, 1000)
        mock_setuid.assert_called_with(1000)

if __name__ == '__main__':
    unittest.main()