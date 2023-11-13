import unittest
from unittest.mock import patch
from your_module import validate_password  # replace 'your_module' with the name of your module

class TestPassword(unittest.TestCase):

    @patch('builtins.input', return_value='Password1$')
    def test_validate_password(self, input):
        self.assertTrue(validate_password(input()))

    @patch('builtins.input', return_value='password')
    def test_validate_password_no_uppercase(self, input):
        self.assertFalse(validate_password(input()))

    @patch('builtins.input', return_value='PASSWORD')
    def test_validate_password_no_lowercase(self, input):
        self.assertFalse(validate_password(input()))

    @patch('builtins.input', return_value='Password')
    def test_validate_password_no_number(self, input):
        self.assertFalse(validate_password(input()))

    @patch('builtins.input', return_value='Password1')
    def test_validate_password_no_special_char(self, input):
        self.assertFalse(validate_password(input()))

if __name__ == '__main__':
    unittest.main()