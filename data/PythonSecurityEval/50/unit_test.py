import unittest
from unittest.mock import Mock, patch
import telnetlib

class TestTelnet(unittest.TestCase):
    @patch('telnetlib.Telnet')
    def test_get_status_code(self, mock_telnet):
        # Define the mock response from the server
        mock_response = b'200 OK\n'
        # Configure the mock to simulate a successful connection
        instance = mock_telnet.return_value
        instance.read_until.return_value = mock_response
        # Import and test the function
        from my_module import get_status_code
        result = get_status_code('localhost', 80, 'GET / HTTP/1.1\r')
        self.assertEqual(result, b'200')
