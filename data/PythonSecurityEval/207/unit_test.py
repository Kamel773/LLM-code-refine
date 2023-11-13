import unittest
from unittest.mock import patch
from flask import url_for
from your_flask_app import app  # replace with your actual Flask app import

class TestRedirect(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('flask.redirect')
    def test_redirect_to_target(self, mock_redirect):
        response = self.app.get('/redirect?target=https://www.google.com')
        mock_redirect.assert_called_once_with('https://www.google.com', code=302)

    @patch('flask.redirect')
    def test_redirect_no_target(self, mock_redirect):
        response = self.app.get('/redirect')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b"No target URL specified")
        mock_redirect.assert_not_called()

if __name__ == '__main__':
    unittest.main()