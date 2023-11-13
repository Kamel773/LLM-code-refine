import unittest
from unittest.mock import patch, Mock
from flask import Flask
from your_flask_app import download_file  # replace 'your_flask_app' with the name of your Flask app file

class TestDownloadFile(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    @patch('flask.send_file')
    def test_download_file(self, mock_send_file):
        mock_send_file.return_value = 'File content'
        response = self.client.get('/download?file=example.txt')
        mock_send_file.assert_called_once_with('example.txt', as_attachment=True)
        self.assertEqual(response.data, b'File content')

if __name__ == '__main__':
    unittest.main()