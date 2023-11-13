import unittest
from unittest import mock

class TestPasswordGenerator(unittest.TestCase):
    @mock.patch('password_generator.random.choice')
    def test_generate_password(self, mock_choice):
        mock_choice.side_effect = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        password = generate_password(length=8)
        self.assertEqual(password, 'ABCDEFGH')

if __name__ == '__main__':
    unittest.main()
