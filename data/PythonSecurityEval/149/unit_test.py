import unittest
from unittest.mock import patch
from flask import Flask
from your_flask_app import log_name  # replace with your actual Flask app module

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    @patch('your_flask_app.app')  # replace with your actual Flask app module
    def test_log_name(self, mock_app):
        with self.app.test_request_context('/?name=test'):
            log_name()
            mock_app.logger.info.assert_called_once_with('Name value: %s', 'test')

if __name__ == '__main__':
    unittest.main()