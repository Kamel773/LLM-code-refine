import unittest
from unittest.mock import patch, Mock
from your_module import extract_urls  # replace 'your_module' with the name of your Python file

class TestExtractUrls(unittest.TestCase):
    @patch('requests.get')
    def test_extract_urls(self, mock_get):
        mock_response = Mock()
        mock_response.text = '<html><body><a href="https://www.example1.com">Example 1</a><a href="https://www.example2.com">Example 2</a></body></html>'
        mock_get.return_value = mock_response

        expected_urls = ['https://www.example1.com', 'https://www.example2.com']
        actual_urls = extract_urls('https://www.example.com')

        self.assertEqual(actual_urls, expected_urls)

if __name__ == '__main__':
    unittest.main()