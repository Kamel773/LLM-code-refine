import unittest
from unittest.mock import Mock, MagicMock
from your_module import register_user

class TestRegisterUser(unittest.TestCase):
    def test_register_user(self):
        # Mock database and cursor
        mock_db = Mock()
        mock_cursor = Mock()
        mock_db.cursor.return_value = mock_cursor

        # Mock existing user
        mock_cursor.fetchone.return_value = None

        # Test register_user function
        result = register_user('testuser', 'testpassword', mock_db)

        # Assert function returned True (user was registered)
        self.assertTrue(result)

        # Assert cursor.execute was called with correct SQL and parameters
        mock_cursor.execute.assert_any_call("SELECT * FROM users WHERE username = %s", ('testuser',))
        mock_cursor.execute.assert_any_call("INSERT INTO users (username, password) VALUES (%s, %s)", ('testuser', ANY))

        # Assert db.commit was called
        mock_db.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()