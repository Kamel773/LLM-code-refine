import unittest
from unittest.mock import patch, MagicMock
from mymodule import get_all_documents  # assuming the function is in a module named mymodule

class TestGetAllDocuments(unittest.TestCase):
    @patch('mymodule.MongoClient')
    def test_get_all_documents(self, mock_client):
        mock_collection = MagicMock()
        mock_db = MagicMock()
        mock_client.return_value.__getitem__.return_value = mock_db
        mock_db.__getitem__.return_value = mock_collection
        mock_collection.find.return_value = [{'_id': '1', 'name': 'John Doe'}]

        result = get_all_documents('mycollection')

        mock_client.assert_called_once_with('localhost', 27017)
        mock_db.__getitem__.assert_called_once_with('mycollection')
        mock_collection.find.assert_called_once_with()
        self.assertEqual(result, [{'_id': '1', 'name': 'John Doe'}])

if __name__ == '__main__':
    unittest.main()