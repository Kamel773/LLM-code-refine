import unittest
from unittest.mock import patch, mock_open
import os

class TestWriteToTempFile(unittest.TestCase):
    @patch('tempfile.NamedTemporaryFile')
    def test_write_to_temp_file(self, mock_temp):
        mock_file = mock_open()
        mock_temp.return_value.__enter__.return_value = mock_file

        unicode_string = "Hello, World!"
        expected_path = "/tmp/tempfile.txt"
        mock_temp.return_value.name = expected_path

        from your_module import write_to_temp_file
        result = write_to_temp_file(unicode_string)

        mock_file().write.assert_called_once_with(unicode_string)
        self.assertEqual(result, expected_path)

if __name__ == '__main__':
    unittest.main()