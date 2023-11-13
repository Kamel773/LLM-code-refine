import unittest
from unittest.mock import patch
from flask import json

class TestHelloRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('flask.request')
    def test_hello(self, mock_request):
        mock_request.args.get.return_value = 'John'
        response = self.app.get('/hello')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Hello, John!')

    @patch('flask.request')
    def test_hello_missing_name(self, mock_request):
        mock_request.args.get.return_value = None
        response = self.app.get('/hello')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Missing name parameter')

    @patch('flask.request')
    def test_hello_non_alphabetic_name(self, mock_request):
        mock_request.args.get.return_value = '123'
        response = self.app.get('/hello')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Name must be alphabetic')

if __name__ == '__main__':
    unittest.main()