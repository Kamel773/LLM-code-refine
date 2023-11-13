import unittest
from unittest.mock import patch

class TestConvertToInt(unittest.TestCase):
    @patch('builtins.input', return_value='10')
    def test_convert_to_int(self, input):
        self.assertEqual(convert_to_int(), 10)

    @patch('builtins.input', return_value='not a number')
    def test_convert_to_int_invalid(self, input):
        self.assertEqual(convert_to_int(), None)

if __name__ == '__main__':
    unittest.main()