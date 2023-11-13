import unittest
from unittest.mock import patch, MagicMock
from pymongo import MongoClient
from your_module import create_mongodb_collection  # replace 'your_module' with the name of your module

class TestCreateMongoDBCollection(unittest.TestCase):
    @patch('your_module.MongoClient')  # replace 'your_module' with the name of your module
    def test_create_mongodb_collection(self, mock_mongo_client):
        mock_db = MagicMock()
        mock_mongo_client.return_value.__getitem__.return_value = mock_db

        db_name = 'test_db'
        collection_name = 'test_collection'
        create_mongodb_collection(db_name, collection_name)

        mock_mongo_client.assert_called_once_with('localhost', 27017)
        mock_db.__getitem__.assert_called_once_with(collection_name)

if __name__ == '__main__':
    unittest.main()