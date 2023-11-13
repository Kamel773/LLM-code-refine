import unittest
from unittest.mock import patch, Mock
from my_module import redirect_to_target_url  # replace 'my_module' with the name of your module

class TestRedirect(unittest.TestCase):
    @patch('my_module.redirect')
    def test_redirect_to_target_url(self, mock_redirect):
        # Arrange
        mock_redirect.return_value = 'Redirected'
        url = 'http://www.example.com'

        # Act
        result = redirect_to_target_url(url)

        # Assert
        mock_redirect.assert_called_once_with(url)
        self.assertEqual(result, 'Redirected')

    @patch('my_module.redirect')
    def test_redirect_to_target_url_invalid(self, mock_redirect):
        # Arrange
        url = 'not a valid url'

        # Act
        result = redirect_to_target_url(url)

        # Assert
        mock_redirect.assert_not_called()
        self.assertEqual(result, 'Invalid URL')

if __name__ == '__main__':
    unittest.main()