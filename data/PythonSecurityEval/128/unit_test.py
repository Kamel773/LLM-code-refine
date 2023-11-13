import unittest
from unittest.mock import patch, mock_open
import os
import tarfile

class TestExtractTarFile(unittest.TestCase):
    @patch('os.path.exists')
    @patch('tarfile.open')
    def test_extract_tar_file(self, mock_tarfile_open, mock_os_path_exists):
        mock_os_path_exists.return_value = True
        mock_tarfile_open.return_value = mock_open()

        result = extract_tar_file('test.tar')

        self.assertTrue(result)
        mock_os_path_exists.assert_called_once_with('/tmp/test.tar')
        mock_tarfile_open.assert_called_once_with('/tmp/test.tar')

    @patch('os.path.exists')
    def test_extract_tar_file_file_not_found(self, mock_os_path_exists):
        mock_os_path_exists.return_value = False

        with self.assertRaises(FileNotFoundError):
            extract_tar_file('test.tar')

        mock_os_path_exists.assert_called_once_with('/tmp/test.tar')

    def test_extract_tar_file_not_tar_file(self):
        with self.assertRaises(ValueError):
            extract_tar_file('test.txt')

if __name__ == '__main__':
    unittest.main()