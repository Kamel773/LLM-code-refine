import unittest
from unittest.mock import patch
from flask import url_for
from your_flask_app import app  # replace 'your_flask_app' with the name of your python file

class TestRedirect(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('flask.redirect')
    def test_redirect_to_url(self, mock_redirect):
        response = self.app.get(url_for('redirect_to_url'))
        mock_redirect.assert_called_once_with(url_for('target_url'))

if __name__ == '__main__':
    unittest.main()