import unittest
from unittest.mock import Mock
from my_module import are_accounts_equal  # assuming the function is in my_module.py

class TestAreAccountsEqual(unittest.TestCase):
    def test_are_accounts_equal(self):
        mock_account1 = Mock()
        mock_account2 = Mock()

        mock_account1.configure_mock(**{'id': 1, 'name': 'John Doe', 'balance': 1000})
        mock_account2.configure_mock(**{'id': 1, 'name': 'John Doe', 'balance': 1000})

        self.assertTrue(are_accounts_equal(mock_account1, mock_account2))

        mock_account2.configure_mock(**{'id': 2, 'name': 'Jane Doe', 'balance': 2000})

        self.assertFalse(are_accounts_equal(mock_account1, mock_account2))

if __name__ == '__main__':
    unittest.main()