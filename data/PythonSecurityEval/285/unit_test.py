import unittest
from unittest.mock import patch, MagicMock
from chat_server import ChatServer

class TestChatServer(unittest.TestCase):
    @patch('socket.socket', return_value=MagicMock())
    def test_start(self, mock_socket):
        server = ChatServer()
        server.start()
        mock_socket.assert_called_with(socket.AF_INET, socket.SOCK_STREAM)
        mock_socket.return_value.bind.assert_called_with((server.host, server.port))
        mock_socket.return_value.listen.assert_called_once()

if __name__ == "__main__":
    unittest.main()