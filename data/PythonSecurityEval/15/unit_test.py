import unittest
from unittest.mock import Mock, patch

class TestRemoveTrailingNewline(unittest.TestCase):
    def test_remove_trailing_newline(self):
        mock_value = Mock()
        mock_value.__str__.return_value = 'Hello, world!\n'
        
        with patch('your_module.remove_trailing_newline', return_value='Hello, world!') as mock_func:
            remove_trailing_newline(mock_value)
            mock_func.assert_called_once_with(mock_value)
