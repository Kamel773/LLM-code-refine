import unittest
from unittest.mock import mock_open, patch

class TestExtractEmails(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="test@example.com\nanother.test@domain.com")
    def test_extract_emails(self, mock_file):
        with patch('builtins.print') as mock_print:
            extract_emails('dummy_file')
            mock_print.assert_any_call('test@example.com')
            mock_print.assert_any_call('another.test@domain.com')

if __name__ == '__main__':
    unittest.main()