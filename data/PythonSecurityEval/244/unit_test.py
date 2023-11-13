import unittest
from unittest.mock import patch, MagicMock
import my_module  # replace with the name of the module where you defined the create_user function

class TestCreateUser(unittest.TestCase):
    @patch('my_module.MongoClient')
    def test_create_user(self, mock_client):
        mock_db = MagicMock()
        mock_client.return_value.__getitem__.return_value = mock_db

        my_module.create_user('testuser', 'testpass', 'testdb')

        mock_client.assert_called_once_with('localhost', 27017)
        mock_client.return_value.__getitem__.assert_called_once_with('testdb')
        mock_db.command.assert_called_once_with('createUser', 'testuser', pwd='testpass', roles=['readWrite'])

if __name__ == '__main__':
    unittest.main()