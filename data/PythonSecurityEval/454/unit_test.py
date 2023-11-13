import unittest
from unittest.mock import patch

class TestValidateInput(unittest.TestCase):
    @patch('builtins.input', return_value='validinput')
    def test_validate_input(self, input):
        self.assertTrue(validate_input(input()))

    @patch('builtins.input', return_value='')
    def test_validate_input_empty(self, input):
        with self.assertRaises(ValueError):
            validate_input(input())

    @patch('builtins.input', return_value='thisinputiswaytoolong')
    def test_validate_input_too_long(self, input):
        with self.assertRaises(ValueError):
            validate_input(input())

    @patch('builtins.input', return_value=123)
    def test_validate_input_not_string(self, input):
        with self.assertRaises(ValueError):
            validate_input(input())

if __name__ == '__main__':
    unittest.main()