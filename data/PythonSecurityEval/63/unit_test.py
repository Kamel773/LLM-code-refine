import unittest
from unittest.mock import patch, call
from django.test import SimpleTestCase

class ToBoldFilterTest(SimpleTestCase):
    @patch('django.utils.safestring.mark_safe')
    def test_to_bold(self, mock_mark_safe):
        # Call the function with a test string
        to_bold('test string')
        
        # Check that mark_safe was called with the correct argument
        mock_mark_safe.assert_called_once_with('<b>test string</b>')

if __name__ == '__main__':
    unittest.main()
