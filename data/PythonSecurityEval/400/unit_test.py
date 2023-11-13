import unittest
from unittest.mock import patch

class TestCrackPassword(unittest.TestCase):
    @patch('hashlib.md5')
    def test_crack_password(self, mock_hash):
        # Mock the hashlib.md5 function to return a known hash
        mock_hash.return_value.hexdigest.return_value = '098f6bcd4621d373cade4e832627b4f6'

        # Create a rainbow table with the known hash
        rainbow_table = {'098f6bcd4621d373cade4e832627b4f6': 'test'}

        # Test the crack_password function
        self.assertEqual(crack_password(rainbow_table, '098f6bcd4621d373cade4e832627b4f6'), 'test')

if __name__ == '__main__':
    unittest.main()