import unittest
from unittest.mock import patch, mock_open
import os

class TestSecureDelete(unittest.TestCase):
    @patch('os.path.exists', return_value=True)
    @patch('os.remove')
    @patch('os.urandom', return_value=b'random')
    @patch('builtins.open', new_callable=mock_open, read_data=b'data')
    def test_secure_delete(self, mock_file, mock_urandom, mock_remove, mock_exists):
        secure_delete('testfile')
        mock_file.assert_called_once_with('testfile', 'ba+')
        handle = mock_file()
        self.assertEqual(handle.write.call_count, 3)
        handle.write.assert_called_with(b'random')
        mock_remove.assert_called_once_with('testfile')

if __name__ == '__main__':
    unittest.main()