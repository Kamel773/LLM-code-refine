import unittest
from unittest.mock import patch, MagicMock
import socket

class TestUDPSocketServer(unittest.TestCase):
    @patch('socket.socket')
    def test_udp_socket_server(self, mock_socket):
        from your_module import udp_socket_server

        mock_sock_instance = MagicMock()
        mock_socket.return_value = mock_sock_instance

        udp_socket_server()

        # Check if socket was created with correct parameters
        mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_DGRAM)

        # Check if bind was called with correct parameters
        mock_sock_instance.bind.assert_called_once_with(('localhost', 12345))

        # Check if recvfrom was called with correct parameters
        mock_sock_instance.recvfrom.assert_called_once_with(4096)

        # Check if sendto was called with correct parameters
        data, address = mock_sock_instance.recvfrom.return_value
        mock_sock_instance.sendto.assert_called_once_with(data, address)

if __name__ == '__main__':
    unittest.main()