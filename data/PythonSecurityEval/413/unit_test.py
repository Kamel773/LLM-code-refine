import unittest
from unittest.mock import patch, MagicMock
import socket
from my_module import connect_to_server  # assuming the function is in a file named my_module.py

class TestConnectToServer(unittest.TestCase):
    @patch('socket.socket')
    def test_connect_to_server(self, mock_socket):
        mock_socket.return_value.connect.return_value = None

        ip = '127.0.0.1'
        port = 8000

        result = connect_to_server(ip, port)

        mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)
        mock_socket.return_value.connect.assert_called_once_with((ip, port))
        self.assertEqual(result, mock_socket.return_value)

if __name__ == '__main__':
    unittest.main()