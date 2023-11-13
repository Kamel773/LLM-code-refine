import unittest
from unittest.mock import patch
from system import System

class TestSystem(unittest.TestCase):
    @patch.object(System, 'users', new_callable=dict)
    def test_create_user(self, mock_users):
        system = System()
        username = 'testuser'
        password = 'testpassword'

        # Test creating a new user
        result = system.create_user(username, password)
        self.assertTrue(result)
        mock_users.__setitem__.assert_called_with(username, password)

        # Test creating a user that already exists
        mock_users.__contains__.return_value = True
        result = system.create_user(username, password)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()