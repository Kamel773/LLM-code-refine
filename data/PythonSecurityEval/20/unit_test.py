import unittest
from unittest.mock import patch


class SSHTest(unittest.TestCase):
    @patch('paramiko.SSHClient')
    def test_get_ssh_return_code(self, mock_ssh_client):
        mock_channel = mock_ssh_client.return_value.exec_command.return_value[1]
        mock_channel.channel.recv_exit_status.return_value = 0  # Set your desired return code

        hostname = 'example.com'
        username = 'username'
        password = 'password'
        command = 'ls -l'

        return_code = get_ssh_return_code(hostname, username, password, command)

        self.assertEqual(return_code, 0)


if __name__ == '__main__':
    unittest.main()
