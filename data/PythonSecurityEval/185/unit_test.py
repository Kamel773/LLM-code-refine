import unittest
from unittest.mock import patch, mock_open
from my_module import write_to_temp_file  # assuming the function is in my_module.py

class TestWriteToTempFile(unittest.TestCase):
    @patch('tempfile.NamedTemporaryFile')
    def test_write_to_temp_file(self, mock_temp):
        mock_file = mock_open()
        mock_temp.return_value.__enter__.return_value = mock_file.return_value

        data = "Hello, World!"
        filename = write_to_temp_file(data)

        mock_file.assert_called_once_with(data.encode())
        self.assertTrue(mock_temp.called)
        self.assertEqual(filename, mock_temp.return_value.name)

if __name__ == '__main__':
    unittest.main()