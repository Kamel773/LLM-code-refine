import unittest
from unittest.mock import patch
import requests

class TestScrapeWebpage(unittest.TestCase):
    @patch('requests.get')
    def test_scrape_webpage(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.text = '<html><body><h1>Hello, World!</h1></body></html>'
        result = scrape_webpage('http://example.com')
        self.assertEqual(result.h1.string, 'Hello, World!')

if __name__ == '__main__':
    unittest.main()