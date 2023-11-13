import unittest
from unittest.mock import patch
from my_module import get_integer_input  # assuming the function is in a module named my_module

class TestGetIntegerInput(unittest.TestCase):
    @patch('builtins.input', return_value='10')
    def test_get_integer_input(self, input):
        self.assertEqual(get_integer_input(), 10)

    @patch('builtins.input', side_effect=['not an integer', '20'])
    def test_get_integer_input_invalid_then_valid(self, input):
        self.assertEqual(get_integer_input(), 20)

if __name__ == '__main__':
    unittest.main()