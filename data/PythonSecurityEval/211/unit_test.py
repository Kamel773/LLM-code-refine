import unittest
from unittest.mock import patch, Mock
import socket
import start_echo_server  # replace 'your_module' with the name of your module

class TestEchoServer(unittest.TestCase):
    @patch('socket.socket')
    def test_start_echo_server(self, mock_socket):
        mock_conn = Mock()
        mock_socket.return_value.__enter__.return_value.accept.return_value = (mock_conn, ('localhost', 12345))
        start_echo_server()
        self.assertTrue(mock_conn.sendall.called)

if __name__ == '__main__':
    unittest.main()