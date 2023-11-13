import unittest
from unittest.mock import patch, MagicMock
from your_module import drop_collection  # replace 'your_module' with the name of the module where you defined the function

class TestDropCollection(unittest.TestCase):
    @patch('your_module.MongoClient')  # replace 'your_module' with the name of the module where you defined the function
    def test_drop_collection(self, mock_client):
        mock_db = MagicMock()
        mock_client.return_value.__getitem__.return_value = mock_db

        drop_collection('test_db', 'test_collection')

        mock_client.assert_called_once_with('localhost', 27017)
        mock_db.__getitem__.assert_called_once_with('test_collection')
        mock_db.__getitem__.return_value.drop.assert_called_once()

if __name__ == '__main__':
    unittest.main()