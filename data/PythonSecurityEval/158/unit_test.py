import unittest
from unittest.mock import patch

class TestPassword(unittest.TestCase):
    @patch('is_valid_password')  # replace 'your_module' with the name of your module
    def test_is_valid_password(self, mock_is_valid_password):
        mock_is_valid_password.return_value = True
        result = is_valid_password('Admin@123')
        self.assertEqual(result, True)

        mock_is_valid_password.return_value = False
        result = is_valid_password('admin')
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()