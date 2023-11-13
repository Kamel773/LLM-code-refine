import unittest
from unittest.mock import patch
from io import StringIO

class TestDecryptString(unittest.TestCase):
    @patch('builtins.input', side_effect=['abc', '1'])
    def test_decrypt_string(self, mock_input):
        self.assertEqual(decrypt_string('abc', 1), 'zab')

if __name__ == '__main__':
    unittest.main()