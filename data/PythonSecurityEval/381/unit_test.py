import unittest
from unittest.mock import mock_open, patch

class TestStorePassword(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_store_password(self, mock_open):
        store_password('test_user', 'test_password')
        mock_open.assert_called_once_with('passwords.txt', 'a')
        handle = mock_open()
        handle.write.assert_called_once_with('test_user:test_password\n')

if __name__ == '__main__':
    unittest.main()