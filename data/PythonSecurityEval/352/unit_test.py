import unittest
from unittest.mock import patch, MagicMock
from your_module import compare_passwords

class TestComparePasswords(unittest.TestCase):
    @patch('your_module.Session')
    def test_compare_passwords(self, mock_session):
        mock_user = MagicMock()
        mock_user.password = 'password'
        mock_session.query().filter_by().first.return_value = mock_user

        result = compare_passwords('username', 'password')

        self.assertTrue(result)

        result = compare_passwords('username', 'wrong_password')

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()