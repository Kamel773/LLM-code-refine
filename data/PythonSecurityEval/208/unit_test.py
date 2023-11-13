import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from your_flask_app import app  # replace with your actual Flask app import

class TestRedirect(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    @patch('flask.request')
    def test_redirect_url(self, mock_request):
        mock_request.args.get.return_value = 'https://www.google.com'
        response = self.client.get(url_for('redirect_url'))
        self.assertRedirects(response, 'https://www.google.com')

    @patch('flask.request')
    def test_redirect_url_no_url(self, mock_request):
        mock_request.args.get.return_value = None
        response = self.client.get(url_for('redirect_url'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_data(as_text=True), "URL not provided")

if __name__ == '__main__':
    unittest.main()