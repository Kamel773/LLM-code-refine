import unittest
from unittest.mock import patch

class TestStorePassword(unittest.TestCase):
    @patch('__main__.passwords', {})
    def test_store_password(self):
        store_password('user1', 'password1')
        self.assertEqual(passwords['user1'], 'password1')

if __name__ == '__main__':
    unittest.main()