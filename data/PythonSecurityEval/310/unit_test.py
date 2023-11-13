import unittest
from unittest.mock import mock_open, patch
import your_module  # replace with the name of the module where you defined the function

class TestReadFileContent(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="test content")
    def test_read_file_content(self, mock_file):
        result = your_module.read_file_content('any_path')  # replace with the name of your module
        self.assertEqual(result, "test content")
        mock_file.assert_called_once_with('any_path', 'r')

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_read_file_content_file_not_found(self, mock_file):
        result = your_module.read_file_content('any_path')  # replace with the name of your module
        self.assertEqual(result, "File not found")

if __name__ == '__main__':
    unittest.main()