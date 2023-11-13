import unittest
from unittest.mock import patch, Mock
from flask import url_for
from your_flask_app import app  # replace 'your_flask_app' with the name of your Flask app module

class TestHomeRoute(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='<h1>Hello, {{name}}!</h1>')
    @patch('flask.render_template_string')
    def test_home(self, mock_render, mock_open):
        response = self.client.get(url_for('home'), query_string={'name': 'John'})
        mock_open.assert_called_once_with('template.html', 'r')
        mock_render.assert_called_once_with('<h1>Hello, {{name}}!</h1>', name='John')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()