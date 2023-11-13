import unittest
from unittest.mock import patch, call
import my_module  # replace with the name of the module where start_server is defined

class TestStartServer(unittest.TestCase):
    @patch('http.server.SimpleHTTPRequestHandler')
    @patch('socketserver.TCPServer')
    def test_start_server(self, mock_TCPServer, mock_SimpleHTTPRequestHandler):
        directory = '.'
        port = 8000

        my_module.start_server(directory, port)

        self.assertEqual(mock_SimpleHTTPRequestHandler.directory, directory)
        mock_TCPServer.assert_called_once_with(("", port), mock_SimpleHTTPRequestHandler)

if __name__ == '__main__':
    unittest.main()