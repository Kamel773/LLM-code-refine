import unittest
from unittest.mock import patch

class TestCrawler(unittest.TestCase):
    @patch('requests.get')
    def test_crawl(self, mock_get):
        crawl('http://example.com', 2)
        mock_get.assert_called_with('http://example.com')

if __name__ == '__main__':
    unittest.main()