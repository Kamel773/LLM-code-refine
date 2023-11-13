import unittest
from unittest.mock import patch, MagicMock, mock_open

class TestUploader(unittest.TestCase):
    @patch('requests.post')
    @patch('builtins.open', new_callable=mock_open, read_data='file_content')
    def test_uploading(self, mock_file, mock_post):

        # Setup the mock
        mock_response = mock_post.return_value
        mock_response.status_code = 200

        # Call the function with test data
        response = uploading('test_file.txt', 'http://testurl.com')

        # Assert that open was called with the right arguments
        mock_file.assert_called_once_with('test_file.txt', 'rb')

        # Assert that requests.post was called with the right arguments
        mock_post.assert_called_once_with('http://testurl.com', files={'file': mock_file()})

        # Assert that the function returned the mock response
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()