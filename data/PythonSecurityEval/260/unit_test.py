import unittest
from unittest.mock import patch, MagicMock
from pymongo import MongoClient
from mymodule import create_document  # assuming the function is in a module named 'mymodule'

class TestCreateDocument(unittest.TestCase):
    @patch('mymodule.MongoClient')
    def test_create_document(self, mock_client):
        mock_collection = MagicMock()
        mock_db = MagicMock()
        mock_client.return_value.__getitem__.return_value = mock_db
        mock_db.__getitem__.return_value = mock_collection
        mock_collection.insert_one.return_value.inserted_id = '12345'

        result = create_document('mycollection', {'key': 'value'})

        mock_client.assert_called_once_with('localhost', 27017)
        mock_db.__getitem__.assert_called_once_with('mycollection')
        mock_collection.insert_one.assert_called_once_with({'key': 'value'})
        self.assertEqual(result, '12345')

if __name__ == '__main__':
    unittest.main()