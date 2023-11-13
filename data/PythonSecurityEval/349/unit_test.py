import unittest
from unittest.mock import patch, Mock
import your_module  # replace with the name of the module where you defined the scrape_urls function

class TestScrapeUrls(unittest.TestCase):
    @patch('requests.get')
    def test_scrape_urls(self, mock_get):
        mock_response = Mock()
        mock_response.text = '<html><body><a href="http://example.com"></a></body></html>'
        mock_get.return_value = mock_response

        expected_urls = ['http://example.com']
        actual_urls = your_module.scrape_urls('http://dummy.com')

        self.assertEqual(actual_urls, expected_urls)

if __name__ == '__main__':
    unittest.main()