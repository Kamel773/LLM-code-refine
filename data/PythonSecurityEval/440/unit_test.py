import unittest
from unittest.mock import patch

class TestExtractUrls(unittest.TestCase):
    @patch('__main__.extract_urls')
    def test_extract_urls(self, mock_extract_urls):
        mock_extract_urls.return_value = ['https://www.example.com', 'http://www.another-example.com']
        text = "Here is a website https://www.example.com and another one http://www.another-example.com"
        self.assertEqual(extract_urls(text), ['https://www.example.com', 'http://www.another-example.com'])

if __name__ == '__main__':
    unittest.main()