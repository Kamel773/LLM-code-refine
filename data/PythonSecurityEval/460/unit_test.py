import unittest
from unittest.mock import patch, Mock
import your_module  # replace with the name of the module where you defined the above function

class TestExtractLinks(unittest.TestCase):
    @patch('requests.get')
    def test_extract_links(self, mock_get):
        mock_response = Mock()
        mock_response.text = '<html><body><a href="http://example.com">link</a></body></html>'
        mock_get.return_value = mock_response

        expected_links = ['http://example.com']
        actual_links = your_module.extract_links('http://dummy.com')

        self.assertEqual(actual_links, expected_links)

if __name__ == '__main__':
    unittest.main()