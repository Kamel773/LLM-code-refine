import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
import your_flask_app  # replace with your actual Flask app module

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    @patch('your_flask_app.request')
    def test_upload_file(self, mock_request):
        mock_file = MagicMock()
        mock_file.read.return_value = b'<root><child>data</child></root>'
        mock_request.files = {'file': mock_file}

        response = self.client.post('/upload')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf8'), '<root><child>data</child></root>')

if __name__ == '__main__':
    unittest.main()