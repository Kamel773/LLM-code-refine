import unittest
from unittest.mock import patch
from flask import json

class TestGetData(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    @patch('flask.request')
    def test_get_data(self, mock_request):
        mock_request.get_json.return_value = {"name": "test"}

        response = self.client.post('/data', 
                                    data=json.dumps({"name": "test"}), 
                                    content_type='application/json')
        
        data = json.loads(response.get_data())
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Data received')
        self.assertEqual(data['received_data'], {"name": "test"})


if __name__ == '__main__':
    unittest.main()
