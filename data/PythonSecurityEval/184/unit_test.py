import unittest
from unittest import mock
from your_module import read_file_content  # replace 'your_module' with the name of your module

class TestReadFileContent(unittest.TestCase):
    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data="file content")
    @mock.patch('os.path.isfile', return_value=True)
    def test_read_file_content(self, mock_isfile, mock_open):
        filename = 'test.txt'
        expected_content = 'file content'
        actual_content = read_file_content(filename)
        self.assertEqual(actual_content, expected_content)
        mock_isfile.assert_called_once_with(filename)
        mock_open.assert_called_once_with(filename, 'r')

if __name__ == '__main__':
    unittest.main()