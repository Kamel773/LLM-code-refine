import unittest
from unittest.mock import patch
from flask import Flask
from your_flask_app import log_error  # replace with your actual Flask app module

class TestLogError(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    @patch('your_flask_app.app.logger')  # replace with your actual Flask app module
    def test_log_error(self, mock_logger):
        response = self.client.get('/log_error?input=test_error')
        mock_logger.error.assert_called_once_with('Error: %s', 'test_error')
        self.assertEqual(response.data, b'Logged error: test_error')

if __name__ == '__main__':
    unittest.main()