import unittest
from unittest.mock import patch, mock_open

class TestScrapeWebpage(unittest.TestCase):
    @patch('requests.get')
    def test_scrape_webpage(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.text = '<span class="chart-element__information__song">Test Song</span><span class="chart-element__information__artist">Test Artist</span>'

        with patch("builtins.open", mock_open()) as mock_file:
            scrape_webpage('https://www.billboard.com/charts/hot-100/')

            mock_file().write.assert_called_with('Test Song,Test Artist\n')

if __name__ == '__main__':
    unittest.main()