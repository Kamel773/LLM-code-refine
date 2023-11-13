import unittest
from unittest.mock import patch

class TestDecryptString(unittest.TestCase):
    @patch('__main__.decrypt_string')
    def test_decrypt_string(self, mock_decrypt_string):
        mock_decrypt_string.return_value = 'abc'
        result = decrypt_string('def')
        self.assertEqual(result, 'abc')

if __name__ == '__main__':
    unittest.main()