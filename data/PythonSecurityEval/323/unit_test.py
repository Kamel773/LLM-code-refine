import unittest
from unittest.mock import patch, MagicMock
import my_module  # replace with the name of the module where connect_to_server is defined

class TestSSHConnection(unittest.TestCase):
    @patch('my_module.paramiko.SSHClient')
    def test_connect_to_server(self, mock_ssh):
        mock_ssh.return_value.connect.return_value = None
        mock_ssh.return_value.close.return_value = None

        server_address = '192.168.1.1'
        username = 'user'
        password = 'pass'

        my_module.connect_to_server(server_address, username, password)

        mock_ssh.return_value.connect.assert_called_once_with(server_address, username=username, password=password)
        mock_ssh.return_value.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()