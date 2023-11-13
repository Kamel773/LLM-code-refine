import unittest
from unittest.mock import patch
from your_module import generate_password

class TestGeneratePassword(unittest.TestCase):
    @patch('your_module.random.choice')
    def test_generate_password(self, mock_choice):
        mock_choice.side_effect = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        result = generate_password(8)
        self.assertEqual(result, 'abcdefgh')

    def test_generate_password_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(7)

    def test_generate_password_non_integer_length(self):
        with self.assertRaises(ValueError):
            generate_password('eight')

if __name__ == '__main__':
    unittest.main()