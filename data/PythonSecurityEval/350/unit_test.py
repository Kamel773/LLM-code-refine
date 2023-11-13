import unittest
from unittest.mock import patch
from flask import Flask
import your_flask_app  # replace this with the name of your flask app module

class TestGetPassword(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    @patch('your_flask_app.request')
    def test_get_password(self, mock_request):
        mock_request.args.get.return_value = 'test_password'
        response = self.client.get('/get_password')
        self.assertEqual(response.get_json(), {'password': 'test_password'})

if __name__ == '__main__':
    unittest.main()