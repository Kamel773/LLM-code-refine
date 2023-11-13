import unittest
from unittest.mock import patch, Mock
from my_module import get_links  # assuming the function is in a module named my_module

class TestGetLinks(unittest.TestCase):
    @patch('requests.get')
    def test_get_links(self, mock_get):
        # Mock the response from requests.get
        mock_response = Mock()
        mock_response.text = '<html><body><a href="http://example.com"></a></body></html>'
        mock_get.return_value = mock_response

        # Call the function with the mock in place
        links = get_links('http://dummy.com')

        # Assert that the function returned the expected result
        self.assertEqual(links, ['http://example.com'])

if __name__ == '__main__':
    unittest.main()