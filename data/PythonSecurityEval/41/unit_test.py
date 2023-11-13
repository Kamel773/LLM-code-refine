import unittest
from unittest.mock import patch

class TestRandomGenerator(unittest.TestCase):

    @patch('os.urandom')
    def test_generate_random_real(self, mock_urandom):
        mock_urandom.return_value = bytes([0, 0, 0, 50])  # This will generate 50 / 429496729.5 as the output

        result = generate_random_real()
        self.assertEqual(result, 50 / 429496729.5)  # Check if the result is as expected

if __name__ == '__main__':
    unittest.main()
