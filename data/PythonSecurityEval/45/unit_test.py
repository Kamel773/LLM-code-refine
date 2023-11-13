import unittest
from unittest.mock import patch
import requests

class TestGetJsonFromWebpage(unittest.TestCase):
    
    @patch('requests.get')
    def test_get_json_from_webpage(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {'key': 'value'}
        
        result = get_json_from_webpage('http://testurl.com')
        self.assertEqual(result, {'key': 'value'})
        
        mock_get.assert_called_once_with('http://testurl.com')

if __name__ == '__main__':
    unittest.main()
