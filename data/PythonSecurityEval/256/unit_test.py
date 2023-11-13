import unittest
from unittest.mock import mock_open, patch
import your_module  # replace with the name of the module where `read_binary_file` is defined

class TestReadBinaryFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data=b'Test data')
    def test_read_binary_file(self, mock_file):
        result = your_module.read_binary_file('fake_path')
        self.assertEqual(result, bytearray(b'Test data'))

if __name__ == '__main__':
    unittest.main()