import unittest
from unittest.mock import patch

class TestRandomFloatBetween(unittest.TestCase):
    @patch('random.uniform')
    def test_random_float_between(self, mock_uniform):
        # Setup
        min_val = 1.0
        max_val = 5.0
        mock_uniform.return_value = 3.0

        # Call the function
        result = random_float_between(min_val, max_val)

        # Assert the function was called with the correct arguments
        mock_uniform.assert_called_once_with(min_val, max_val)

        # Assert the result is as expected
        self.assertEqual(result, 3.0)

    def test_random_float_between_with_invalid_range(self):
        # Assert that ValueError is raised for invalid range
        with self.assertRaises(ValueError):
            random_float_between(5.0, 1.0)

if __name__ == '__main__':
    unittest.main()
