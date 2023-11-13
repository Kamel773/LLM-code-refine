import unittest
from unittest.mock import patch, call
import your_module  # replace with your actual module name

class TestExecuteCommand(unittest.TestCase):
    @patch('subprocess.Popen')
    def test_execute_command(self, mock_subprocess):
        command = 'echo Hello, World!'
        your_module.execute_command(command)

        mock_subprocess.assert_called_once_with(command, shell=True, stdout=subprocess.PIPE)
        assert mock_subprocess.return_value.communicate.called

if __name__ == '__main__':
    unittest.main()