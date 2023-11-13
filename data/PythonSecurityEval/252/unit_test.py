import unittest
from unittest.mock import patch, MagicMock
import paramiko
import your_module  # replace with the name of your module

class TestSSHConnect(unittest.TestCase):
    @patch('paramiko.SSHClient')
    def test_ssh_connect(self, mock_ssh):
        # Arrange
        mock_ssh.return_value.connect.return_value = None
        server_ip = '192.168.1.1'
        username = 'user'
        password = 'pass'

        # Act
        result = your_module.ssh_connect(server_ip, username, password)

        # Assert
        mock_ssh.return_value.connect.assert_called_once_with(server_ip, username=username, password=password)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()