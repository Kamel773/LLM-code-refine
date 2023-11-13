import unittest
from unittest.mock import patch, MagicMock
import pam
import your_module  # replace with the name of your module

class TestAuthenticateUser(unittest.TestCase):
    @patch.object(pam.pam, 'authenticate')
    def test_authenticate_user(self, mock_authenticate):
        # Arrange
        mock_authenticate.return_value = True
        username = 'testuser'
        password = 'testpassword'

        # Act
        result = your_module.authenticate_user(username, password)

        # Assert
        self.assertTrue(result)
        mock_authenticate.assert_called_once_with(username, password)

if __name__ == '__main__':
    unittest.main()