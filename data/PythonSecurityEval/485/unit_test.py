import unittest
from unittest.mock import patch

def get_password():
    password = input("Enter your password: ")
    print(password)

class TestGetPassword(unittest.TestCase):
    @patch('builtins.input', return_value='mypassword')
    @patch('builtins.print')
    def test_get_password(self, mock_print, mock_input):
        get_password()
        mock_input.assert_called_once_with("Enter your password: ")
        mock_print.assert_called_once_with('mypassword')

if __name__ == '__main__':
    unittest.main()