import unittest
from unittest.mock import patch, MagicMock
import my_module  # replace with the name of the module where start_server is defined

class TestServer(unittest.TestCase):
    @patch('http.server.SimpleHTTPRequestHandler')
    @patch('socketserver.TCPServer')
    def test_start_server(self, mock_server, mock_handler):
        mock_server_instance = mock_server.return_value
        mock_handler_instance = mock_handler.return_value

        my_module.start_server()

        mock_server.assert_called_once_with(("", 8000), mock_handler)
        mock_server_instance.serve_forever.assert_called_once()

if __name__ == '__main__':
    unittest.main()