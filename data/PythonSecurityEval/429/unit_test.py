import unittest
from unittest.mock import patch, call
from my_module import send_encrypted_message  # assuming the function is in a module named my_module

class TestSendEncryptedMessage(unittest.TestCase):
    @patch('socket.socket')
    def test_send_encrypted_message(self, mock_socket):
        message = 'Hello, World!'
        key = Fernet.generate_key()
        host = 'localhost'
        port = 12345

        send_encrypted_message(message, key, host, port)

        mock_socket.assert_has_calls([
            call().connect((host, port)),
            call().sendall(message.encode())
        ])

if __name__ == '__main__':
    unittest.main()