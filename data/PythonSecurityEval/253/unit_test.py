import unittest
from unittest.mock import patch

class TestDecryptString(unittest.TestCase):
    @patch('builtins.input', return_value='dpef')
    def test_decrypt_string(self, input):
        self.assertEqual(decrypt_string(input(), 1), 'code')

if __name__ == '__main__':
    unittest.main()