import unittest
from unittest.mock import patch

class TestEncryptString(unittest.TestCase):
    @patch('builtins.input', return_value='abc')
    def test_encrypt_string(self, input):
        self.assertEqual(encrypt_string('abc', 3), 'def')

if __name__ == '__main__':
    unittest.main()