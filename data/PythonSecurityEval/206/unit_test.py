import unittest
from unittest.mock import patch
from flask import url_for
from your_flask_app import app  # replace with your actual Flask app import

class TestRedirect(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('flask.redirect')
    def test_redirect_user(self, mock_redirect):
        response = self.app.get(url_for('redirect_user'))
        mock_redirect.assert_called_once_with("http://www.example.com", code=302)

if __name__ == "__main__":
    unittest.main()