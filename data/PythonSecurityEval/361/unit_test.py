import unittest
from unittest.mock import mock_open, patch
from my_module import open_file  # assuming the function is in a module named my_module

class TestOpenFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="test data")
    def test_open_file(self, mock_file):
        result = open_file("any_path")  # the path doesn't matter because we're mocking the open function
        self.assertEqual(result, "test data")

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_open_file_not_found(self, mock_file):
        result = open_file("any_path")  # the path doesn't matter because we're mocking the open function
        self.assertEqual(result, "File not found.")

if __name__ == '__main__':
    unittest.main()