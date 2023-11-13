import unittest
from unittest.mock import patch
from flask_login import current_user
from flask import url_for
from your_flask_app import app, User

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()

    @patch('your_flask_app.User')
    def test_login(self, mock_user):
        mock_user.return_value = User('1')
        with self.client:
            response = self.client.get('/login', follow_redirects=True)
            self.assertTrue(current_user.is_authenticated)
            self.assertEqual(response.status_code, 200)

    @patch('your_flask_app.User')
    def test_logout(self, mock_user):
        mock_user.return_value = User('1')
        with self.client:
            self.client.get('/login', follow_redirects=True)
            response = self.client.get('/logout', follow_redirects=True)
            self.assertFalse(current_user.is_authenticated)
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()