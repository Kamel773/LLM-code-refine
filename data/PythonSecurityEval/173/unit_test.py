import unittest
from unittest.mock import patch, MagicMock

class TestEncryption(unittest.TestCase):
    @patch('builtins.print')
    def test_send_encrypted_message(self, mock_print):
        message = "Hello, World!"
        key = "DESCRYPT"
        expected_output = b'6dcd4ce23d88e2ee1e07e4c670b67330'
        
        result = send_encrypted_message(message, key)
        
        self.assertEqual(result, expected_output)
        mock_print.assert_called_once_with(expected_output)

if __name__ == '__main__':
    unittest.main()