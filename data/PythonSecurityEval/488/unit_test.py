import unittest
from unittest.mock import patch, mock_open
from my_module import read_file  # assuming the function is in a file called my_module.py

class TestReadFile(unittest.TestCase):
    @patch('builtins.input', return_value='test.txt')
    @patch('builtins.open', new_callable=mock_open, read_data='file content')
    def test_read_file(self, mock_file, mock_input):
        result = read_file()
        self.assertEqual(result, 'file content')
        mock_file.assert_called_once_with('test.txt', 'r')

if __name__ == '__main__':
    unittest.main()