import unittest
from unittest.mock import patch
import logging

class TestConvertInputToInt(unittest.TestCase):
    @patch('builtins.input', return_value='123')
    def test_convert_input_to_int_success(self, input):
        self.assertEqual(convert_input_to_int(input()), 123)

    @patch('builtins.input', return_value='abc')
    @patch.object(logging, 'error')
    def test_convert_input_to_int_failure(self, mock_logging, input):
        self.assertIsNone(convert_input_to_int(input()))
        mock_logging.assert_called_once_with("Conversion error: Input was not a valid integer.")

if __name__ == '__main__':
    unittest.main()