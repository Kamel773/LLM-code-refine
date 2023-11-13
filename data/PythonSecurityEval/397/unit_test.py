import unittest
from unittest.mock import patch, MagicMock
from pymongo import MongoClient
import your_module  # replace with the name of your module

class TestMongoDBConnection(unittest.TestCase):
    @patch('your_module.MongoClient')
    def test_connect_to_mongodb(self, mock_client):
        mock_client.return_value = MagicMock(spec=MongoClient)
        connection_string = "mongodb://localhost:27017/"
        result = your_module.connect_to_mongodb(connection_string)
        mock_client.assert_called_once_with(connection_string)
        self.assertEqual(result, mock_client.return_value)

if __name__ == '__main__':
    unittest.main()