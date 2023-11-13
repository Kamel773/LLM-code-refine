import unittest
from unittest.mock import patch
from flask import url_for
from your_flask_app import app  # replace with your actual Flask app

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('your_flask_app.EXPECTED_PASSWORD', 'test_password')  # replace with your actual Flask app
    def test_login_success(self):
        response = self.app.get('/login?password=test_password')
        self.assertEqual(response.status_code, 302)  # 302 status code for redirect
        self.assertTrue("/home" in response.location)  # check if it redirects to home

    @patch('your_flask_app.EXPECTED_PASSWORD', 'test_password')  # replace with your actual Flask app
    def test_login_fail(self):
        response = self.app.get('/login?password=wrong_password')
        self.assertEqual(response.status_code, 401)  # 401 status code for unauthorized

if __name__ == '__main__':
    unittest.main()