import unittest
from unittest.mock import patch
from user_account import UserAccount

class TestUserAccount(unittest.TestCase):
    @patch.object(UserAccount, 'users', return_value={'existing_user': 'password123'})
    def test_create_user_existing(self, _):
        user_account = UserAccount()
        response = user_account.create_user('existing_user')
        self.assertEqual(response, 'Username already exists')

    @patch.object(UserAccount, 'users', return_value={})
    def test_create_user_new(self, _):
        user_account = UserAccount()
        response = user_account.create_user('new_user')
        self.assertEqual(response, 'User created successfully')

if __name__ == '__main__':
    unittest.main()