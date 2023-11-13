import unittest
from unittest.mock import Mock, patch

class TestUser(unittest.TestCase):
    @patch.object(User, 'has_role', return_value=True)
    def test_access_resource_granted(self, mock_has_role):
        user = User([])
        self.assertEqual(user.access_resource('admin'), "Access granted")
        mock_has_role.assert_called_once_with('admin')

    @patch.object(User, 'has_role', return_value=False)
    def test_access_resource_denied(self, mock_has_role):
        user = User([])
        self.assertEqual(user.access_resource('admin'), "Access denied")
        mock_has_role.assert_called_once_with('admin')

if __name__ == '__main__':
    unittest.main()