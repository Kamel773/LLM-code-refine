import unittest
from unittest.mock import mock_open, patch
from my_module import get_words_from_file  # assuming the function is in a module named my_module

class TestGetWordsFromFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="This is a test file")
    def test_get_words_from_file(self, mock_file):
        expected_words = ['This', 'is', 'a', 'test', 'file']
        result = get_words_from_file('test.txt')
        self.assertEqual(result, expected_words)

if __name__ == '__main__':
    unittest.main()