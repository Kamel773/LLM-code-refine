import unittest
from unittest.mock import patch

class TestExecuteCode(unittest.TestCase):
    @patch('builtins.exec')
    def test_execute_code(self, mock_exec):
        code = "print('Hello, World!')"
        execute_code(code)
        mock_exec.assert_called_once_with(code)

if __name__ == '__main__':
    unittest.main()