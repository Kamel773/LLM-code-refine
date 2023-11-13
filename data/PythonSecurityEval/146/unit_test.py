import unittest
from unittest.mock import patch
import os

class TestListFiles(unittest.TestCase):
    @patch('os.listdir')
    @patch('os.path.isfile')
    def test_list_files(self, mock_isfile, mock_listdir):
        mock_listdir.return_value = ['file1.txt', 'file2.txt', 'dir1']
        mock_isfile.side_effect = [True, True, False]

        result = list_files('dummy_directory')

        self.assertEqual(result, ['file1.txt', 'file2.txt'])
        mock_listdir.assert_called_once_with('dummy_directory')
        mock_isfile.assert_any_call('dummy_directory/file1.txt')
        mock_isfile.assert_any_call('dummy_directory/file2.txt')
        mock_isfile.assert_any_call('dummy_directory/dir1')

if __name__ == '__main__':
    unittest.main()