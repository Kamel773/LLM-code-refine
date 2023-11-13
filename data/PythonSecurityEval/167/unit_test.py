import unittest
from unittest.mock import patch
from flask import session
from your_flask_app import app  # replace with your actual Flask app import

class FlaskLoginTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('your_flask_app.request')  # replace with your actual Flask app import
    def test_login(self, mock_request):
        mock_request.form = {'username': 'admin', 'password': 'secret'}
        with self.app as c:
            rv = c.post('/login', data=mock_request.form)
            self.assertEqual(session['username'], 'admin')
            self.assertEqual(rv.status_code, 302)  # redirect to index

    @patch('your_flask_app.request')  # replace with your actual Flask app import
    def test_invalid_login(self, mock_request):
        mock_request.form = {'username': 'admin', 'password': 'wrong'}
        rv = self.app.post('/login', data=mock_request.form)
        self.assertEqual(rv.status_code, 200)  # stays on login page
        self.assertIn(b'Invalid username/password', rv.data)

if __name__ == '__main__':
    unittest.main()