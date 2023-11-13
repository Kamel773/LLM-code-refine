import unittest
from unittest.mock import patch

class TestMarkFirst20Chars(unittest.TestCase):
    
    @patch('django.utils.safestring.mark_safe', autospec=True)
    def test_mark_first_20_chars(self, mock_mark_safe):
        text = 'This is a test text string that is long enough to be more than twenty characters.'
        expected_output = text[:20]

        mark_first_20_chars(text)

        # Assert mark_safe() is called once
        self.assertEqual(mock_mark_safe.call_count, 1)

        # Assert mark_safe() is called with correct argument
        mock_mark_safe.assert_called_once_with(expected_output)

if __name__ == '__main__':
    unittest.main()