import unittest
from unittest import mock
import os

class TestCreateUserDirectory(unittest.TestCase):
    @mock.patch('os.makedirs')
    def test_create_user_directory(self, mock_makedirs):
        username = "testuser"
        expected_path = os.path.join("/home", username)
        result = create_user_directory(username)
        mock_makedirs.assert_called_once_with(expected_path, exist_ok=True)
        self.assertEqual(result, expected_path)

    def test_create_user_directory_invalid_username(self):
        with self.assertRaises(ValueError):
            create_user_directory("invalid/username")

if __name__ == "__main__":
    unittest.main()