import unittest
from unittest.mock import patch, MagicMock

class TestExecutePythonCode(unittest.TestCase):
    @patch('builtins.exec')
    def test_execute_python_code(self, mock_exec):
        code = 'print("Hello World!")'
        
        execute_python_code(code)
        
        mock_exec.assert_called_once_with(code)

    @patch('builtins.exec')
    def test_execute_python_code_exception(self, mock_exec):
        mock_exec.side_effect = Exception('Test Exception')
        code = 'print("Hello World!")'
        
        result = execute_python_code(code)
        
        self.assertEqual(result, 'Test Exception')

if __name__ == "__main__":
    unittest.main()