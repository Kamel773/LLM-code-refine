import unittest
from unittest.mock import patch
from flask import url_for
from your_flask_app import app  # replace with the name of your Flask app module

class TestGetSubdomainData(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    @patch('requests.get')
    def test_get_subdomain_data(self, mock_get):
        mock_get.return_value.text = 'Mock response'
        response = self.client.get(url_for('get_subdomain_data', subdomain='test'))
        self.assertEqual(response.data.decode(), 'Mock response')

if __name__ == '__main__':
    unittest.main()