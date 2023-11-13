import unittest
from unittest.mock import patch, MagicMock
from your_module import parse_json_to_mongodb  # replace 'your_module' with the name of your module

class TestParseJsonToMongodb(unittest.TestCase):
    @patch('your_module.MongoClient')  # replace 'your_module' with the name of your module
    @patch('your_module.json.load')
    @patch('your_module.open', new_callable=MagicMock)
    def test_parse_json_to_mongodb(self, mock_open, mock_json_load, mock_mongo_client):
        mock_json_load.return_value = [{'key': 'value'}]
        mock_mongo_client.return_value.__getitem__.return_value.__getitem__.return_value.insert_many.return_value = True

        result = parse_json_to_mongodb('test.json', 'test_db', 'test_collection')

        mock_open.assert_called_once_with('test.json')
        mock_json_load.assert_called_once()
        mock_mongo_client.assert_called_once_with('localhost', 27017)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()