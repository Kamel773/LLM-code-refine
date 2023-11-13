import unittest
from unittest.mock import patch
import os

class TestCheckFileExists(unittest.TestCase):
    @patch('os.path.isfile')
    def test_check_file_exists(self, mock_isfile):
        # Arrange
        mock_isfile.return_value = True
        directory = '/path/to/directory'
        filename = 'file.txt'

        # Act
        result = check_file_exists(directory, filename)

        # Assert
        mock_isfile.assert_called_once_with(os.path.join(directory, filename))
        self.assertTrue(result)

    @patch('os.path.isfile')
    def test_check_file_does_not_exist(self, mock_isfile):
        # Arrange
        mock_isfile.return_value = False
        directory = '/path/to/directory'
        filename = 'file.txt'

        # Act
        result = check_file_exists(directory, filename)

        # Assert
        mock_isfile.assert_called_once_with(os.path.join(directory, filename))
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()