import unittest
from unittest.mock import patch
from flask import Flask
from your_flask_app import get_user_info  # replace with your actual module name

class TestGetUserInfo(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    @patch('your_flask_app.request')  # replace with your actual module name
    def test_get_user_info(self, mock_request):
        mock_request.args = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com'
        }

        with self.app.test_request_context():
            result = get_user_info()
            self.assertEqual(result, {
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'john.doe@example.com'
            })

if __name__ == '__main__':
    unittest.main()