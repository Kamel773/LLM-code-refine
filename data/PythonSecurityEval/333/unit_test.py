import unittest
from unittest.mock import patch, Mock
import base64

class TestDecodeBase64(unittest.TestCase):
    @patch('base64.b64decode')
    def test_decode_base64(self, mock_b64decode):
        test_data = b'Test data'
        mock_b64decode.return_value = test_data

        from your_module import decode_base64  # replace 'your_module' with the name of your module
        result = decode_base64(test_data)
        self.assertEqual(result, test_data)
        mock_b64decode.assert_called_once_with(test_data)

if __name__ == '__main__':
    unittest.main()