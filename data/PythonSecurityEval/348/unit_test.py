import unittest
from unittest.mock import patch, mock_open
from your_module import upload_file  # replace 'your_module' with the name of your module

class TestUploadFile(unittest.TestCase):
    @patch('requests.post')
    @patch('builtins.open', new_callable=mock_open, read_data='file_content')
    def test_upload_file(self, mock_file, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 200

        response = upload_file('http://example.com', 'test_file')

        mock_file.assert_called_once_with('test_file', 'rb')
        mock_post.assert_called_once_with('http://example.com', files={'file': mock_file.return_value})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()