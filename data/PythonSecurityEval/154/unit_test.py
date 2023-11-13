import unittest
from unittest.mock import patch
from flask import Flask
import your_flask_app  # replace with the name of your flask app file

class TestBadRoute(unittest.TestCase):
    def setUp(self):
        self.app = your_flask_app.app.test_client()

    @patch('your_flask_app.do_computation')
    def test_bad_route(self, mock_do_computation):
        mock_do_computation.return_value = 'Computation result'
        response = self.app.get('/bad')
        self.assertEqual(response.data.decode(), 'Computation result')

    @patch('your_flask_app.do_computation')
    def test_bad_route_exception(self, mock_do_computation):
        mock_do_computation.side_effect = Exception('Test exception')
        response = self.app.get('/bad')
        self.assertIn('Test exception', response.data.decode())

if __name__ == '__main__':
    unittest.main()