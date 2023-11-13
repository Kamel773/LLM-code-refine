import unittest
from unittest.mock import patch
import io
import sys

class TestPrintProcessorTime(unittest.TestCase):
    @patch('time.process_time')
    def test_print_processor_time(self, mock_process_time):
        # Arrange
        mock_process_time.return_value = 12345.67
        expected_output = "12345.67\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Act
        print_processor_time()

        # Assert
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()