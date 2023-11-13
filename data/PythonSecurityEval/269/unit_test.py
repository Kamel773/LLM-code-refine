import unittest
from unittest import mock
from zipfile import ZipFile

class TestZipDirectory(unittest.TestCase):
    @mock.patch('zipfile.ZipFile')
    @mock.patch('os.walk')
    def test_zip_directory(self, mock_os_walk, mock_zipfile):
        mock_os_walk.return_value = [
            ('/path/to/dir', ('subdir1', 'subdir2'), ('file1', 'file2')),
        ]
        zip_directory('/path/to/dir', '/path/to/zipfile.zip')
        mock_zipfile.assert_called_once_with('/path/to/zipfile.zip', 'w', zipfile.ZIP_DEFLATED)
        handle = mock_zipfile.return_value.__enter__.return_value
        handle.write.assert_any_call('/path/to/dir/file1')
        handle.write.assert_any_call('/path/to/dir/file2')

if __name__ == '__main__':
    unittest.main()