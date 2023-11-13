import unittest
from unittest.mock import mock_open, patch
from my_module import write_to_file  # assuming the function is in my_module.py

class TestWriteToFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_write_to_file(self, mock_open_instance):
        data = 'Hello, World!'
        file_path = '/path/to/file'

        write_to_file(file_path, data)

        mock_open_instance.assert_called_once_with(file_path, 'w')
        mock_open_instance().write.assert_called_once_with(data)

if __name__ == '__main__':
    unittest.main()