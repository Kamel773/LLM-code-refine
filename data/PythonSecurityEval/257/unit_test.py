import unittest
from unittest.mock import patch, MagicMock
from pymongo import MongoClient, Database

class TestMongoDBConnection(unittest.TestCase):
    @patch('pymongo.MongoClient')
    def test_connect_to_mongodb(self, mock_client):
        mock_db = MagicMock(spec=Database)
        mock_client.return_value.__getitem__.return_value = mock_db

        host = 'localhost'
        port = 27017
        db_name = 'test_db'

        result = connect_to_mongodb(host, port, db_name)

        mock_client.assert_called_once_with(host, port)
        mock_client.return_value.__getitem__.assert_called_once_with(db_name)
        self.assertEqual(result, mock_db)

if __name__ == '__main__':
    unittest.main()