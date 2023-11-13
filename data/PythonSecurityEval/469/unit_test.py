import unittest
from unittest.mock import mock_open, patch
from your_module import read_large_file  # replace 'your_module' with the name of your module

class TestReadLargeFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='line1\nline2\nline3\n')
    def test_read_large_file(self, mock_file):
        file_path = 'test.txt'
        file_generator = read_large_file(file_path)
        self.assertEqual(next(file_generator), 'line1\n')
        self.assertEqual(next(file_generator), 'line2\n')
        self.assertEqual(next(file_generator), 'line3\n')

if __name__ == '__main__':
    unittest.main()