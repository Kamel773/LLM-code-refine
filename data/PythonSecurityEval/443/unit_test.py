import unittest
from unittest import mock
from my_module import connect_to_server  # assuming the function is in my_module.py

class TestSSHConnection(unittest.TestCase):
    @mock.patch('paramiko.SSHClient')
    def test_connect_to_server(self, MockSSH):
        # Create a mock SSH client instance
        mock_client = MockSSH.return_value

        # Call the function with mock data
        client = connect_to_server('hostname', 22, 'username', 'password')

        # Check if the function called the correct methods on the SSH client
        MockSSH.assert_called_once()
        mock_client.set_missing_host_key_policy.assert_called_once_with(paramiko.AutoAddPolicy())
        mock_client.connect.assert_called_once_with('hostname', 22, 'username', 'password')

        # Check if the function returned the correct value
        self.assertEqual(client, mock_client)

if __name__ == '__main__':
    unittest.main()