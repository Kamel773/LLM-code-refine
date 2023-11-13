import unittest
from unittest.mock import patch, Mock
from my_module import get_webpage_title  # assuming the function is in a module named my_module

class TestGetWebpageTitle(unittest.TestCase):
    @patch('my_module.requests.get')
    def test_get_webpage_title(self, mock_get):
        # Mock the response from requests.get
        mock_response = Mock()
        mock_get.return_value = mock_response
        mock_response.text = '<html><head><title>Test Page</title></head><body></body></html>'

        # Call the function with the mocked requests.get
        title = get_webpage_title('http://test.com')

        # Assert that the function returned the correct title
        self.assertEqual(title, 'Test Page')

if __name__ == '__main__':
    unittest.main()