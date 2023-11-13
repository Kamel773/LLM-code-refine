import unittest
from unittest.mock import patch, Mock
from my_module import execute_command  # assuming the function is in a file named my_module.py

class TestExecuteCommand(unittest.TestCase):
    @patch('subprocess.run')
    def test_execute_command(self, mock_run):
        # Mock the subprocess.run function to return a successful result
        mock_run.return_value = Mock(stdout=b'test output', stderr=b'', returncode=0)

        result = execute_command('echo Hello, World!')
        self.assertEqual(result, 'test output')

        # Mock the subprocess.run function to return an error
        mock_run.return_value = Mock(stdout=b'', stderr=b'test error', returncode=1)

        result = execute_command('invalid command')
        self.assertEqual(result, 'test error')

if __name__ == '__main__':
    unittest.main()