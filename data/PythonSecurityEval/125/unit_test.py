import unittest
from unittest.mock import patch, mock_open
import os

class TestDeleteImage(unittest.TestCase):
    @patch('os.path.isfile')
    @patch('os.remove')
    def test_delete_image(self, mock_remove, mock_isfile):
        # Simulate the case where the file exists
        mock_isfile.return_value = True
        self.assertTrue(delete_image('existing_file.jpg'))
        mock_remove.assert_called_once_with('existing_file.jpg')

        # Reset the mock objects
        mock_remove.reset_mock()
        mock_isfile.reset_mock()

        # Simulate the case where the file does not exist
        mock_isfile.return_value = False
        self.assertFalse(delete_image('non_existing_file.jpg'))
        mock_remove.assert_not_called()

if __name__ == '__main__':
    unittest.main()