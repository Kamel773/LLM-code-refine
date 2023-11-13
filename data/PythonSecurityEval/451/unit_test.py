import unittest
from unittest.mock import patch
from your_module import validate_email  # replace 'your_module' with the name of your module

class TestValidateEmail(unittest.TestCase):
    @patch('your_module.re.match')  # replace 'your_module' with the name of your module
    def test_validate_email(self, mock_re):
        mock_re.return_value = True
        result = validate_email('test@example.com')
        self.assertTrue(result)

        mock_re.return_value = False
        result = validate_email('invalid_email')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()