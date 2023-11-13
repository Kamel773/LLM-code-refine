import unittest
from unittest.mock import patch
from my_module import get_integer_input  # assuming the function is in a module named my_module

class TestGetIntegerInput(unittest.TestCase):
    @patch('builtins.input', side_effect=['a', 'b', '3'])
    def test_get_integer_input(self, mock_input):
        result = get_integer_input()
        self.assertEqual(result, 3)
        self.assertEqual(mock_input.call_count, 3)

if __name__ == '__main__':
    unittest.main()