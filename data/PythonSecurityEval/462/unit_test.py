import unittest
from unittest.mock import patch
from flask import json
from my_flask_app import create_app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

    @patch('my_flask_app.create_app')
    def test_hello(self, mock_create_app):
        mock_create_app.return_value = {'message': 'Hello, World!'}, 200
        res = self.client().get('/hello')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['message'], 'Hello, World!')

if __name__ == "__main__":
    unittest.main()