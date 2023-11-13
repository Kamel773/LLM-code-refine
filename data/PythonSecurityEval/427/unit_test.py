import unittest
from unittest.mock import mock_open, patch
from my_module import open_file_in_write_mode  # assuming the function is in my_module.py

class TestOpenFileInWriteMode(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_open_file_in_write_mode(self, mock_open_instance):
        filename = 'test_file.txt'
        open_file_in_write_mode(filename)
        mock_open_instance.assert_called_once_with(filename, 'w')

if __name__ == '__main__':
    unittest.main()