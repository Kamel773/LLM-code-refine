import unittest
from unittest.mock import patch, Mock
import requests

class TestXPathQuery(unittest.TestCase):
    @patch('requests.get')
    def test_xpath_query(self, mock_get):
        mock_response = Mock()
        mock_get.return_value = mock_response
        mock_response.content = b'<root><child>test</child></root>'
        
        result = xpath_query('http://example.com', '/root/child')
        
        self.assertEqual(result[0].text, 'test')

if __name__ == '__main__':
    unittest.main()