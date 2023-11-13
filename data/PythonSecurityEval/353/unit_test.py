import unittest
from unittest.mock import patch, call

class TestRunScript(unittest.TestCase):
    @patch('builtins.exec')
    def test_run_script(self, mock_exec):
        script = 'print("Hello, {}!")'
        args = ('World',)
        run_script(script, args)
        mock_exec.assert_called_once_with(script.format(*args))

if __name__ == '__main__':
    unittest.main()