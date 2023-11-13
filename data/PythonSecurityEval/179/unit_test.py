import unittest
from unittest.mock import patch
from random import choice

class TestRandomString(unittest.TestCase):
    @patch('random.choice')
    def test_generate_random_string(self, mock_choice):
        mock_choice.side_effect = ['a', 'b', 'c', 'd', 'e']
        result = generate_random_string(5)
        self.assertEqual(result, 'abcde')

if __name__ == '__main__':
    unittest.main()