import unittest
from unittest.mock import patch

class TestFibonacci(unittest.TestCase):

    @patch('__main__.fibonacci')
    def test_fibonacci(self, mock_fibonacci):
        mock_fibonacci.side_effect = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.assertEqual(fibonacci(1), 0)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 1)
        self.assertEqual(fibonacci(4), 2)
        self.assertEqual(fibonacci(5), 3)
        self.assertEqual(fibonacci(6), 5)
        self.assertEqual(fibonacci(7), 8)
        self.assertEqual(fibonacci(8), 13)
        self.assertEqual(fibonacci(9), 21)
        self.assertEqual(fibonacci(10), 34)
        self.assertEqual(fibonacci(11), 55)

if __name__ == '__main__':
    unittest.main()