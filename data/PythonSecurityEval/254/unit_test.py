import unittest
from unittest.mock import mock_open, patch

class TestReadFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="test content")
    def test_read_file(self, mock_file):
        result = read_file('fake_path')
        self.assertEqual(result, "test content")

if __name__ == '__main__':
    unittest.main()