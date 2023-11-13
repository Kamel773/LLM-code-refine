import unittest
from unittest.mock import patch, mock_open
import re

class TestFindRegexMatches(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='Hello World')
    @patch('re.findall', return_value=['Hello', 'World'])
    def test_find_regex_matches(self, mock_findall, mock_open):
        find_regex_matches('dummy.txt', r'\w+')
        mock_open.assert_called_once_with('dummy.txt', 'r')
        mock_findall.assert_called_once_with(r'\w+', 'Hello World')

if __name__ == '__main__':
    unittest.main()