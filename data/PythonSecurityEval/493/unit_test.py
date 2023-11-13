import unittest
from unittest.mock import patch, Mock
from flask import Flask

class TestFileUpload(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['UPLOAD_FOLDER'] = '/path/to/upload/folder'
        self.client = self.app.test_client()

    @patch('flask.send_from_directory')
    def test_uploaded_file(self, mock_send_from_directory):
        filename = 'testfile.txt'
        mock_send_from_directory.return_value = 'File content'

        response = self.client.get('/uploads/' + filename)

        mock_send_from_directory.assert_called_once_with(self.app.config['UPLOAD_FOLDER'], filename)
        self.assertEqual(response.data, b'File content')

if __name__ == '__main__':
    unittest.main()