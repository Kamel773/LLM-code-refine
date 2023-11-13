import unittest
from unittest.mock import patch

class TestBlacklistCheck(unittest.TestCase):
    @patch('blacklist', ['192.168.0.1', '10.0.0.1'])
    def test_is_blacklisted(self, mock_blacklist):
        self.assertTrue(is_blacklisted('192.168.0.1', mock_blacklist))
        self.assertFalse(is_blacklisted('127.0.0.1', mock_blacklist))

if __name__ == '__main__':
    unittest.main()