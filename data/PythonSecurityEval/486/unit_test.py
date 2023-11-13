import unittest
from unittest.mock import patch, call

class TestExecuteCommand(unittest.TestCase):
    @patch('subprocess.check_output')
    def test_execute_command(self, mock_subprocess):
        execute_command('ls')
        mock_subprocess.assert_called_once_with('ls', shell=True)

if __name__ == '__main__':
    unittest.main()