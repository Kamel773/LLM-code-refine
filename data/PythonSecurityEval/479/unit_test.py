import unittest
from unittest.mock import patch, MagicMock
import my_module  # replace with the name of the module where connect_to_server is defined

class TestMyModule(unittest.TestCase):
    @patch('my_module.paramiko.SSHClient')
    def test_connect_to_server(self, mock_ssh):
        mock_ssh.return_value.connect.return_value = True
        result = my_module.connect_to_server()
        self.assertTrue(result)
        mock_ssh.return_value.connect.assert_called_once_with('hostname', username='username', password='password')

if __name__ == '__main__':
    unittest.main()