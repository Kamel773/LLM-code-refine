import unittest
from unittest.mock import patch
from io import StringIO

class TestExecuteCode(unittest.TestCase):
    @patch('builtins.exec')
    def test_execute_code(self, mock_exec):
        user_code = 'print("Hello, World!")'
        execute_code(user_code)
        mock_exec.assert_called_once_with(user_code)

    @patch('sys.stdout', new_callable=StringIO)
    def test_execute_code_output(self, mock_stdout):
        user_code = 'print("Hello, World!")'
        execute_code(user_code)
        self.assertEqual(mock_stdout.getvalue(), 'Hello, World!\n')

    def test_execute_code_error(self):
        user_code = 'print(Hello, World!)'  # Syntax error: missing quotes
        result = execute_code(user_code)
        self.assertEqual(result, "name 'Hello' is not defined")

if __name__ == '__main__':
    unittest.main()