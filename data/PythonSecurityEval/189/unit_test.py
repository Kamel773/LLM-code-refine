import unittest
from unittest.mock import patch, call

class TestCreateUdpSocket(unittest.TestCase):
    @patch('socket.socket')
    def test_create_udp_socket(self, mock_socket):
        create_udp_socket("127.0.0.1", 53)
        mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_DGRAM)
        mock_socket.return_value.bind.assert_called_once_with(("127.0.0.1", 53))

if __name__ == '__main__':
    unittest.main()