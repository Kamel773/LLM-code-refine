import unittest
from unittest.mock import patch
import your_module  # replace with the name of the module where retrieve_account_info is defined

class TestRetrieveAccountInfo(unittest.TestCase):
    @patch('your_module.is_user_authorized')
    @patch('your_module.get_account_info')
    def test_retrieve_account_info(self, mock_get_account_info, mock_is_user_authorized):
        # Set up the mock objects
        mock_is_user_authorized.return_value = True
        mock_get_account_info.return_value = {'account_number': '12345678', 'balance': 1000.00}

        # Call the function with a test user_id
        result = your_module.retrieve_account_info('test_user')

        # Check that the mock functions were called with the correct arguments
        mock_is_user_authorized.assert_called_once_with('test_user')
        mock_get_account_info.assert_called_once_with('test_user')

        # Check that the function returned the correct result
        self.assertEqual(result, {'account_number': '12345678', 'balance': 1000.00})

if __name__ == '__main__':
    unittest.main()