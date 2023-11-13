import unittest
from unittest.mock import patch

class TestEncryptString(unittest.TestCase):
    @patch('builtins.input', side_effect=['Hello, World!', 3])
    def test_encrypt_string(self, mock_input):
        self.assertEqual(encrypt_string('Hello, World!', 3), 'Khoor, Zruog!')

if __name__ == '__main__':
    unittest.main()