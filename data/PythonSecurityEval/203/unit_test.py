import unittest
from unittest.mock import patch

class TestPasswordCheck(unittest.TestCase):
    @patch('__main__.mock_db', new_callable=dict)
    def test_check_password(self, mock_db):
        mock_db.update({'user1': 'password1', 'user2': 'password2'})
        self.assertTrue(check_password('user1', 'password1', mock_db))
        self.assertFalse(check_password('user1', 'wrongpassword', mock_db))
        self.assertFalse(check_password('nonexistentuser', 'password1', mock_db))

if __name__ == '__main__':
    unittest.main()