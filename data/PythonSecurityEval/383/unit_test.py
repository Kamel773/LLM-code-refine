import unittest
from unittest.mock import patch, call
import socket
from my_module import open_server_socket  # assuming the function is in my_module.py

class TestOpenServerSocket(unittest.TestCase):
    @patch('socket.socket')
    def test_open_server_socket(self, mock_socket):
        mock_socket.return_value.bind.return_value = None
        mock_socket.return_value.listen.return_value = None

        open_server_socket('localhost', 8080)

        calls = [call(socket.AF_INET, socket.SOCK_STREAM),
                 call().bind(('localhost', 8080)),
                 call().listen(5)]
        mock_socket.assert_has_calls(calls)

if __name__ == '__main__':
    unittest.main()