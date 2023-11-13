import unittest
from unittest.mock import patch, Mock

class TestExecutePythonInline(unittest.TestCase):
    
    @patch('subprocess.Popen')
    def test_execute_python_inline_success(self, mock_popen):
        # Arrange
        mock_process = Mock()
        mock_process.communicate.return_value = (b'Hello, World!', b'')
        mock_process.returncode = 0
        mock_popen.return_value = mock_process

        # Act
        result = your_module.execute_python_inline("print('Hello, World!')")

        # Assert
        self.assertEqual(result, 'Hello, World!')

    @patch('subprocess.Popen')
    def test_execute_python_inline_error(self, mock_popen):
        # Arrange
        mock_process = Mock()
        mock_process.communicate.return_value = (b'', b'Error message')
        mock_process.returncode = 1
        mock_popen.return_value = mock_process

        # Act
        result = your_module.execute_python_inline("print('Hello, World!')")

        # Assert
        self.assertEqual(result, 'Error: Error message')

if __name__ == '__main__':
    unittest.main()
