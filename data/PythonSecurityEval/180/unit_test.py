import unittest
from unittest.mock import patch
import os

class TestGenerateKey(unittest.TestCase):
    @patch('os.urandom')
    def test_generate_key(self, mock_urandom):
        mock_urandom.return_value = b'\x00'*16
        result = generate_key()
        self.assertEqual(result, b'\x00'*16)
        mock_urandom.assert_called_once_with(16)

if __name__ == '__main__':
    unittest.main()