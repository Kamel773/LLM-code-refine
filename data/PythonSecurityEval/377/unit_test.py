import unittest
from unittest.mock import patch, Mock
import your_module  # replace with the name of your module

class TestScrapeAndStore(unittest.TestCase):
    @patch('your_module.requests.get')
    @patch('your_module.sqlite3.connect')
    def test_scrape_and_store(self, mock_sqlite3, mock_requests):
        mock_response = Mock()
        mock_response.text = '<html><head><title>Test Title</title></head></html>'
        mock_requests.return_value = mock_response

        mock_conn = Mock()
        mock_sqlite3.return_value = mock_conn

        your_module.scrape_and_store('http://test.com')

        mock_requests.assert_called_once_with('http://test.com')
        mock_sqlite3.assert_called_once_with('web_data.db')
        mock_conn.cursor().execute.assert_called_with("INSERT INTO web_data VALUES (?)", ('Test Title',))

if __name__ == '__main__':
    unittest.main()