from unittest.mock import patch, Mock
import socket
import pickle

class TestSocketFunctions(unittest.TestCase):
    @patch('socket.socket')
    @patch('pickle.dumps')
    def test_send_obj(self, mock_dumps, mock_socket):
        mock_socket_instance = mock_socket.return_value
        mock_dumps.return_value = b'serialized_obj'

        send_obj('object', 'localhost', 12345)

        mock_dumps.assert_called_once_with('object')
        mock_socket_instance.connect.assert_called_once_with(('localhost', 12345))
        mock_socket_instance.sendall.assert_called_once_with(b'serialized_obj')

    @patch('socket.socket')
    @patch('pickle.loads')
    def test_recv_obj(self, mock_loads, mock_socket):
        mock_socket_instance = mock_socket.return_value
        mock_conn_instance = Mock()
        mock_socket_instance.accept.return_value = (mock_conn_instance, ('localhost', 12345))
        mock_conn_instance.recv.return_value = b'serialized_obj'
        mock_loads.return_value = 'object'

        result = recv_obj('localhost', 12345)

        self.assertEqual(result, 'object')
        mock_loads.assert_called_once_with(b'serialized_obj')

if __name__ == '__main__':
    unittest.main()
