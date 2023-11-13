import unittest
from unittest.mock import patch
import sys

class TestLoadModule(unittest.TestCase):
    @patch('importlib.import_module')
    def test_load_module(self, mock_import):
        from load_module import load_module

        # Test when module is found
        mock_import.return_value = 'mock_module'
        result = load_module('os')
        self.assertEqual(result, 'mock_module')

        # Test when module is not found
        mock_import.side_effect = ImportError
        result = load_module('non_existent_module')
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()