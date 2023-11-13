import unittest
from unittest.mock import patch
from flask import json
from app import app

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('re.search')
    def test_search(self, mock_search):
        mock_search.return_value.group.return_value = 'test'
        response = self.app.post('/search', data=json.dumps({'text': 'test text', 'pattern': 'test'}), content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['result'], 'found')
        self.assertEqual(data['match'], 'test')

    @patch('re.search')
    def test_search_not_found(self, mock_search):
        mock_search.return_value = None
        response = self.app.post('/search', data=json.dumps({'text': 'test text', 'pattern': 'not found'}), content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['result'], 'not found')

if __name__ == '__main__':
    unittest.main()