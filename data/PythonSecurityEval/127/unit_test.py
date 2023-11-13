import unittest
from unittest.mock import patch, Mock
from flask import Flask
from your_flask_app import get_file  # replace 'your_flask_app' with the name of your Flask app file

class TestGetFile(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    @patch('flask.send_file')
    def test_get_file(self, mock_send_file):
        mock_send_file.return_value = 'File data'
        with self.app.test_request_context('/get_file?file_name=test.txt'):
            response = get_file()
        self.assertEqual(response, 'File data')

    @patch('flask.send_file')
    def test_get_file_error(self, mock_send_file):
        mock_send_file.side_effect = Exception('Error message')
        with self.app.test_request_context('/get_file?file_name=test.txt'):
            response = get_file()
        self.assertEqual(response, 'Error message')

if __name__ == '__main__':
    unittest.main()