import unittest
from unittest import mock
import os

class TestCreateDirectory(unittest.TestCase):
    @mock.patch('os.path')
    @mock.patch('os')
    def test_create_directory(self, mock_os, mock_path):
        mock_path.exists.return_value = False

        create_directory('test_dir')

        mock_os.makedirs.assert_called_once_with('test_dir')

    @mock.patch('os.path')
    @mock.patch('os')
    def test_create_directory_already_exists(self, mock_os, mock_path):
        mock_path.exists.return_value = True

        create_directory('test_dir')

        mock_os.makedirs.assert_not_called()

if __name__ == '__main__':
    unittest.main()