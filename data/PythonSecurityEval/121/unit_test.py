import unittest
from unittest.mock import patch
from flask import Flask
from your_flask_app import get_username  # replace with your actual Flask app module

class TestGetUsername(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    @patch('your_flask_app.request')  # replace with your actual Flask app module
    def test_get_username(self, mock_request):
        mock_request.args.get.return_value = 'testuser'
        with self.app.test_request_context():
            response = get_username()
        self.assertEqual(response, {'username': 'testuser'})

if __name__ == '__main__':
    unittest.main()