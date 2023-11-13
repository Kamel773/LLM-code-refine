import unittest
from unittest.mock import patch, Mock
import scrape_data

class TestScrapeData(unittest.TestCase):
    @patch('requests.get')
    def test_scrape_data(self, mock_get):
        mock_response = Mock()
        mock_response.text = '<html><body><table><tr><td>Country</td><td>Capital</td></tr><tr><td>USA</td><td>Washington D.C.</td></tr></table></body></html>'
        mock_get.return_value = mock_response

        scrape_data.scrape_data('https://example.com')

        mock_get.assert_called_once_with('https://example.com')

if __name__ == '__main__':
    unittest.main()