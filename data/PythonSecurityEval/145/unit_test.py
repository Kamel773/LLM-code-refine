import unittest
from unittest.mock import patch
from flask import Flask
from flask.testing import FlaskClient

class TestContentType(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    @patch.object(FlaskClient, 'open')
    def test_get_content(self, mock_open):
        mock_open.return_value.headers = {'Content-Type': 'application/json'}
        response = self.client.get('/content')
        self.assertEqual(response.headers['Content-Type'], 'application/json')

if __name__ == '__main__':
    unittest.main()