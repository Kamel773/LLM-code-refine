import unittest
from unittest.mock import Mock
import base64

class TestDecodeAndCall(unittest.TestCase):
    def test_decode_and_call(self):
        mock_func = Mock(return_value='mocked function called')
        encoded_str = base64.b64encode('test string'.encode('utf-8'))

        result = decode_and_call(mock_func, encoded_str)

        mock_func.assert_called_once_with('test string')
        self.assertEqual(result, 'mocked function called')

if __name__ == '__main__':
    unittest.main()