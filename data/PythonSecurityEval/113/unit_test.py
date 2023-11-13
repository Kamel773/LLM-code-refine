import unittest
from unittest.mock import patch, MagicMock
import paramiko

class TestSSHCommand(unittest.TestCase):
    @patch('paramiko.SSHClient')
    def test_ssh_command(self, mock_ssh):
        mock_ssh.return_value.exec_command.return_value = (None, MagicMock(), None)
        mock_ssh.return_value.exec_command.return_value[1].read.return_value = b'output'

        from ssh_command_module import ssh_command  # replace with your module name
        output = ssh_command('hostname', 22, 'username', 'password', 'command')

        self.assertEqual(output, b'output')
        mock_ssh.return_value.connect.assert_called_once_with('hostname', 22, 'username', 'password')
        mock_ssh.return_value.exec_command.assert_called_once_with('command')
        mock_ssh.return_value.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()