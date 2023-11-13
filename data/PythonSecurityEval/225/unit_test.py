import unittest
from unittest.mock import patch, Mock
import re

class TestSearchText(unittest.TestCase):
    @patch('re.search')
    def test_search_text(self, mock_search):
        # Arrange
        mock_search.return_value = Mock(spec=re.Match)
        pattern = 'hello'
        text = 'hello world'

        # Act
        result = search_text(pattern, text)

        # Assert
        mock_search.assert_called_once_with(pattern, text)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()