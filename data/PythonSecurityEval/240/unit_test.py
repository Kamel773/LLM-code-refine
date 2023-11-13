import unittest
from unittest.mock import mock_open, patch
import my_module  # replace with the name of the module where you defined the function

class TestExtractEmails(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='test@example.com\nanother.test@domain.com')
    def test_extract_emails(self, mock_file):
        expected_emails = ['test@example.com', 'another.test@domain.com']
        result = my_module.extract_emails('fake_path')
        self.assertEqual(result, expected_emails)

if __name__ == '__main__':
    unittest.main()