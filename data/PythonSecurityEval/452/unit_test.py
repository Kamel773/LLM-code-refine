import unittest
from unittest.mock import mock_open, patch
from my_module import read_file_content  # assuming the function is in my_module.py

class TestReadFileContent(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="test content")
    def test_read_file_content(self, mock_file):
        result = read_file_content("any_path")  # the path doesn't matter as we're mocking the file opening
        self.assertEqual(result, "test content")

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_read_file_content_file_not_found(self, mock_file):
        result = read_file_content("any_path")  # the path doesn't matter as we're mocking the file opening
        self.assertEqual(result, "File not found")

if __name__ == '__main__':
    unittest.main()