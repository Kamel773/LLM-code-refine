import unittest
from unittest import mock
from unittest.mock import MagicMock
import os

class TestCreateDirectory(unittest.TestCase):
    @mock.patch('os.mkdir')
    def test_create_directory(self, mock_mkdir):
        mock_mkdir.return_value = None
        result = create_directory("/path/to/new/directory")
        self.assertTrue(result)
        mock_mkdir.assert_called_once_with("/path/to/new/directory")

    @mock.patch('os.mkdir')
    def test_create_directory_exception(self, mock_mkdir):
        mock_mkdir.side_effect = Exception("An error occurred")
        result = create_directory("/path/to/new/directory")
        self.assertFalse(result)
        mock_mkdir.assert_called_once_with("/path/to/new/directory")

if __name__ == '__main__':
    unittest.main()