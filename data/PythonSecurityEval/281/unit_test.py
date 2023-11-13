import unittest
from unittest.mock import patch
import my_http_server  # assuming the above server code is saved in my_http_server.py

class TestMyHttpServer(unittest.TestCase):
    @patch('socketserver.TCPServer')
    def test_run_server(self, mock_server):
        my_http_server.run_server(8000)
        mock_server.assert_called_once_with(("", 8000), http.server.SimpleHTTPRequestHandler)

if __name__ == "__main__":
    unittest.main()