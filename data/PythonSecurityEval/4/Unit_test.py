import unittest
from unittest.mock import patch, MagicMock, mock_open

class TestReadingFromText(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="Test data")
    def test_Reading_from_text(self, mock_file):
        result = Reading_from_text("any_path")  # the file path does not matter as the function is being mocked
        self.assertEqual(result, "Test data")

if __name__ == '__main__':
    unittest.main()