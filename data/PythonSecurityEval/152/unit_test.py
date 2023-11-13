import unittest
from unittest.mock import patch, call
from my_module import increment_array_elements  # assuming the function is in my_module.py

class TestIncrementArrayElements(unittest.TestCase):
    @patch('__main__.increment_array_elements')
    def test_increment_array_elements(self, mock_increment_array_elements):
        test_array = [1, 2, 3, 4, 5]
        increment_array_elements(test_array)
        mock_increment_array_elements.assert_called_once_with(test_array)
        self.assertEqual(mock_increment_array_elements.return_value, [2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()