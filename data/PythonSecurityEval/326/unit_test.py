import unittest
from unittest.mock import patch, mock_open, MagicMock

class TestScrapeAndSave(unittest.TestCase):
    @patch('requests.get')
    @patch('csv.writer')
    def test_scrape_and_save(self, mock_csv_writer, mock_requests_get):
        mock_response = MagicMock()
        mock_requests_get.return_value = mock_response

        mock_soup = MagicMock()
        mock_table = MagicMock()
        mock_rows = [MagicMock(), MagicMock()]
        mock_table.find_all.return_value = mock_rows
        mock_soup.find.return_value = mock_table
        mock_response.text = '<html></html>'
        mock_csv_file = mock_open()

        with patch('builtins.open', mock_csv_file):
            scrape_and_save('http://example.com', 'test.csv')

        mock_requests_get.assert_called_once_with('http://example.com')
        mock_csv_writer().writerows.assert_called_once()

if __name__ == '__main__':
    unittest.main()