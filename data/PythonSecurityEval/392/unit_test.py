import unittest
from unittest.mock import mock_open, patch

class TestWriteToFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_write_to_file(self, mock_open):
        write_to_file('test.txt', 'Hello, World!')
        mock_open.assert_called_once_with('test.txt', 'w')
        mock_open().write.assert_called_once_with('Hello, World!')

if __name__ == '__main__':
    unittest.main()