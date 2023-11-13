import unittest
from unittest.mock import mock_open, patch

class TestOpenFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="test data")
    def test_open_file(self, mock_file):
        from your_module import open_file  # replace 'your_module' with the name of your module
        result = open_file('any/path')  # the path doesn't matter because we're mocking the open function
        self.assertEqual(result, "test data")

if __name__ == '__main__':
    unittest.main()