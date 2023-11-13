import unittest
from unittest.mock import mock_open, patch
from my_module import read_file  # assuming the function is in a module named my_module

class TestReadFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="test data")
    def test_read_file(self, mock_open):
        result = read_file("any_path")  # the path doesn't matter because we're mocking open
        self.assertEqual(result, "test data")

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_read_file_not_found(self, mock_open):
        result = read_file("any_path")  # the path doesn't matter because we're mocking open
        self.assertEqual(result, "File not found")

if __name__ == '__main__':
    unittest.main()