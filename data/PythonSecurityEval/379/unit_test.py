import unittest
from unittest.mock import patch
from your_module import generate_password

class TestGeneratePassword(unittest.TestCase):
    @patch('your_module.random.choice')
    def test_generate_password(self, mock_choice):
        mock_choice.return_value = 'a'
        password = generate_password(5, 1)
        self.assertEqual(password, 'aaaaa')

        mock_choice.return_value = 'A'
        password = generate_password(5, 2)
        self.assertEqual(password, 'AAAAA')

        mock_choice.return_value = '1'
        password = generate_password(5, 3)
        self.assertEqual(password, '11111')

        mock_choice.return_value = '!'
        password = generate_password(5, 4)
        self.assertEqual(password, '!!!!!')

        with self.assertRaises(ValueError):
            generate_password(5, 5)

if __name__ == '__main__':
    unittest.main()