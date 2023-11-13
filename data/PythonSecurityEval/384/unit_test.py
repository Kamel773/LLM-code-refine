import unittest
from unittest.mock import mock_open, patch
import your_module  # replace with the name of the module where you defined the read_file function

class TestReadFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="test data")
    @patch('os.path.exists', return_value=True)
    def test_read_file(self, mock_exists, mock_open):
        result = your_module.read_file('any/path')  # replace with the name of your module
        self.assertEqual(result, "test data")
        mock_open.assert_called_once_with('any/path', 'r')

    @patch('os.path.exists', return_value=False)
    def test_read_file_not_found(self, mock_exists):
        result = your_module.read_file('any/path')  # replace with the name of your module
        self.assertEqual(result, "File not found")

if __name__ == '__main__':
    unittest.main()