import unittest
from unittest.mock import patch
from flask import url_for
from myapp import app  # replace 'myapp' with the name of your python file

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('myapp.request')  # replace 'myapp' with the name of your python file
    def test_greet(self, mock_request):
        mock_request.args.get.return_value = 'Test'
        response = self.app.get(url_for('greet'))
        self.assertIn(b'Hello, Test!', response.data)

if __name__ == '__main__':
    unittest.main()