import unittest
from unittest.mock import patch
import string

class TestPasswordGenerator(unittest.TestCase):
    @patch('random.choice')
    def test_generate_password(self, mock_choice):
        mock_choice.side_effect = ['a', 'b', 'c', '1', '2', '3', '!', '@', '#']
        expected_password = 'abc123!@#'
        actual_password = generate_password(9)
        self.assertEqual(actual_password, expected_password)

if __name__ == '__main__':
    unittest.main()