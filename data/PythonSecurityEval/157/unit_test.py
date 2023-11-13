import unittest
from unittest.mock import patch, MagicMock

class TestParseString(unittest.TestCase):
    @patch('builtins.input', return_value='a,b,c,d,e')
    def test_parse_string(self, input):
        self.assertEqual(parse_string(input()), 5)

if __name__ == '__main__':
    unittest.main()