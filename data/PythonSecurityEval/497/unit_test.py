import unittest
from unittest.mock import patch, Mock
import subprocess

class TestRunCommand(unittest.TestCase):
    @patch('subprocess.Popen')
    def test_run_command(self, mock_popen):
        command = 'echo Hello, World!'
        process_mock = Mock()
        attrs = {'communicate.return_value': ('output', 'error')}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value = process_mock
        stdout, stderr = run_command(command)
        self.assertEqual(stdout, 'output')
        self.assertEqual(stderr, 'error')

if __name__ == '__main__':
    unittest.main()