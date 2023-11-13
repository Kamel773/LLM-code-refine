import unittest
from unittest.mock import patch, MagicMock

class TestCreateUser(unittest.TestCase):
    @patch('django.contrib.auth.models.User.objects.create_user')
    def test_create_user(self, mock_create_user):
        mock_user = MagicMock()
        mock_create_user.return_value = mock_user

        username = 'testuser'
        password = 'testpassword'

        result = create_user(username, password)

        mock_create_user.assert_called_once_with(username=username, password=password)
        self.assertEqual(result, mock_user)

if __name__ == '__main__':
    unittest.main()