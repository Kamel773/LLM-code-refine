import unittest
from unittest.mock import patch
from your_module import validate_password  # replace 'your_module' with the name of your module

class TestValidatePassword(unittest.TestCase):
    @patch('your_module.validate_password')  # replace 'your_module' with the name of your module
    def test_validate_password(self, mock_validate_password):
        mock_validate_password.return_value = True
        result = validate_password('password123', 'password123')
        self.assertTrue(result)

        mock_validate_password.return_value = False
        result = validate_password('password123', 'password124')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()