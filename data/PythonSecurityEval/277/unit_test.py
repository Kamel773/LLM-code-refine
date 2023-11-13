import unittest
from unittest.mock import patch, Mock

class TestGetLinks(unittest.TestCase):
    @patch('requests.get')
    def test_get_links(self, mock_get):
        mock_response = Mock()
        mock_response.text = '<html><body><a href="http://example.com">Example</a></body></html>'
        mock_get.return_value = mock_response

        expected_links = ['http://example.com']
        actual_links = get_links('http://dummy.com')

        self.assertEqual(actual_links, expected_links)

if __name__ == '__main__':
    unittest.main()