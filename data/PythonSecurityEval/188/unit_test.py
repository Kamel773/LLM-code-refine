import unittest
from unittest.mock import patch
import os

class TestSearchUsernameInFilename(unittest.TestCase):

    @patch('os.path.basename')
    def test_search_username_in_filename(self, mock_basename):
        mock_basename.return_value = 'username_file.txt'

        result = search_username_in_filename('username', '/path/to/username_file.txt')

        self.assertTrue(result)
        mock_basename.assert_called_once_with('/path/to/username_file.txt')

if __name__ == '__main__':
    unittest.main()