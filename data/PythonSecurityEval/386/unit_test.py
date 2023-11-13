import unittest
from unittest.mock import patch, MagicMock
from my_module import remove_first_document  # assuming the function is in a file called my_module.py

class TestRemoveFirstDocument(unittest.TestCase):
    @patch('my_module.MongoClient')
    def test_remove_first_document(self, mock_client):
        mock_collection = MagicMock()
        mock_client.return_value.__getitem__.return_value.__getitem__.return_value = mock_collection

        remove_first_document('test_collection')

        mock_collection.find_one.assert_called_once()
        mock_collection.delete_one.assert_called_once()

if __name__ == '__main__':
    unittest.main()