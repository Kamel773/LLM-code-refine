import unittest
from unittest.mock import patch, Mock
import socket
import ssl
import your_module  # replace with your actual module name

class TestCreateSslSocket(unittest.TestCase):
    @patch('ssl.create_default_context')
    @patch('socket.socket')
    def test_create_ssl_socket(self, mock_socket, mock_ssl_context):
        mock_ssl_socket = Mock()
        mock_context = Mock()
        mock_context.wrap_socket.return_value = mock_ssl_socket
        mock_ssl_context.return_value = mock_context

        host = 'localhost'
        port = 12345

        result = your_module.create_ssl_socket(host, port)

        mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)
        mock_ssl_context.assert_called_once_with(ssl.Purpose.CLIENT_AUTH)
        mock_context.wrap_socket.assert_called_once_with(mock_socket.return_value, server_hostname=host)
        mock_ssl_socket.connect.assert_called_once_with((host, port))
        self.assertEqual(result, mock_ssl_socket)

if __name__ == '__main__':
    unittest.main()