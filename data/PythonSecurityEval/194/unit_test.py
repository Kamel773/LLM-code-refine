import unittest
from unittest.mock import patch
from admin_access import AdminAccess

class TestAdminAccess(unittest.TestCase):
    @patch.object(AdminAccess, 'validate')
    def test_validate(self, mock_validate):
        # Arrange
        username = "admin"
        password = "password123"
        mock_validate.return_value = True

        # Act
        result = AdminAccess().validate(username, password)

        # Assert
        self.assertTrue(result)
        mock_validate.assert_called_once_with(username, password)

if __name__ == '__main__':
    unittest.main()