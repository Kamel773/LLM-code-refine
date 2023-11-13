import unittest
from unittest.mock import patch
import secrets

class TestGeneratePassword(unittest.TestCase):
    @patch('secrets.choice')
    def test_generate_password(self, mock_choice):
        mock_choice.side_effect = ['a', 'b', 'c', '1', '2', '3', '!', '@', '#', '$']
        result = generate_password(10)
        self.assertEqual(result, 'abc123!@#$')

if __name__ == '__main__':
    unittest.main()