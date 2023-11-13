import unittest
from unittest.mock import patch, Mock
from your_module import extract_hyperlinks  # replace 'your_module' with the name of your module

class TestExtractHyperlinks(unittest.TestCase):
    @patch('requests.get')
    def test_extract_hyperlinks(self, mock_get):
        mock_response = Mock()
        mock_response.text = '<html><body><a href="http://example.com"></a></body></html>'
        mock_get.return_value = mock_response

        expected_links = ['http://example.com']
        actual_links = extract_hyperlinks('http://dummy.com')

        self.assertEqual(actual_links, expected_links)

if __name__ == '__main__':
    unittest.main()