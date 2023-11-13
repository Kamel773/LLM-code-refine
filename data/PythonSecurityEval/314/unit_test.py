import unittest
from unittest.mock import patch
import os

class TestCreateDirectory(unittest.TestCase):
    @patch('os.makedirs')
    def test_create_directory(self, mock_makedirs):
        path = "/path/to/new/directory"
        result = create_directory(path)
        mock_makedirs.assert_called_once_with(path)
        self.assertTrue(result)

    @patch('os.makedirs')
    def test_create_existing_directory(self, mock_makedirs):
        mock_makedirs.side_effect = FileExistsError
        path = "/path/to/existing/directory"
        result = create_directory(path)
        mock_makedirs.assert_called_once_with(path)
        self.assertFalse(result)

    @patch('os.makedirs')
    def test_create_directory_with_error(self, mock_makedirs):
        mock_makedirs.side_effect = Exception
        path = "/path/to/new/directory"
        result = create_directory(path)
        mock_makedirs.assert_called_once_with(path)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()