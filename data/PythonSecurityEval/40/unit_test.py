import unittest
from unittest.mock import patch
import random

class TestMultipleRandomChoice(unittest.TestCase):

    @patch('random.choice', return_value='a')
    def test_multiple_random_choice(self, mock_choice):
        lst = ['a', 'b', 'c', 'd', 'e']
        result = multiple_random_choice(lst, n=3)
        self.assertEqual(result, ['a', 'a', 'a'])
        self.assertEqual(mock_choice.call_count, 3)

if __name__ == '__main__':
    unittest.main()
