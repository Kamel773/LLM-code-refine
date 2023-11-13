import unittest
from unittest.mock import patch
import re

class TestValidateEmail(unittest.TestCase):

    @patch('re.search')
    def test_validate_email(self, mock_search):
        mock_search.return_value = True
        result = validate_email('test@example.com')
        self.assertTrue(result)
        mock_search.assert_called_once_with('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', 'test@example.com')

        mock_search.return_value = False
        result = validate_email('invalid_email')
        self.assertFalse(result)
        mock_search.assert_called_with('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', 'invalid_email')

if __name__ == '__main__':
    unittest.main()