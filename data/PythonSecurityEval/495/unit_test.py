import unittest
from unittest.mock import mock_open, patch

class TestPrintFileContents(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="test content")
    def test_print_file_contents(self, mock_file):
        with patch('builtins.print') as mock_print:
            print_file_contents("testfile")
            mock_file.assert_called_once_with("testfile", 'r')
            mock_print.assert_called_once_with("test content")

if __name__ == '__main__':
    unittest.main()