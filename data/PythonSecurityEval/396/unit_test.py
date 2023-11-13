import unittest
from unittest.mock import patch
from flask import json
from my_flask_app import app  # replace with the name of your Flask app file

class FlaskTest(unittest.TestCase):
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_post_data(self, mock_open):
        tester = app.test_client(self)
        response = tester.post('/data', data=json.dumps({'key': 'value'}), content_type='application/json')
        mock_open().write.assert_called_once_with('{"key": "value"}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Success!')

if __name__ == '__main__':
    unittest.main()