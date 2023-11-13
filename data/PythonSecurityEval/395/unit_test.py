import unittest
from unittest.mock import mock_open, patch

class TestExecuteFile(unittest.TestCase):
    @patch("builtins.exec")
    @patch("builtins.open", new_callable=mock_open, read_data="print('Hello, World!')")
    def test_execute_file(self, mock_open, mock_exec):
        execute_file("testfile")
        mock_open.assert_called_once_with("testfile", 'r')
        mock_exec.assert_called_once_with("print('Hello, World!)")

if __name__ == '__main__':
    unittest.main()