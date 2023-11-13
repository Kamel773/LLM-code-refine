import unittest
from unittest.mock import patch, MagicMock
import xml.etree.ElementTree as ET
from pymongo import MongoClient

class TestParseXmlToMongodb(unittest.TestCase):
    @patch('xml.etree.ElementTree.parse')
    @patch('pymongo.MongoClient')
    def test_parse_xml_to_mongodb(self, mock_mongo_client, mock_et_parse):
        # Arrange
        mock_root = MagicMock()
        mock_et_parse.return_value.getroot.return_value = mock_root
        mock_collection = MagicMock()
        mock_mongo_client.return_value.__getitem__.return_value.__getitem__.return_value = mock_collection

        # Act
        parse_xml_to_mongodb('test.xml', 'test_db', 'test_collection')

        # Assert
        mock_et_parse.assert_called_once_with('test.xml')
        mock_mongo_client.assert_called_once_with('localhost', 27017)
        mock_mongo_client.return_value.__getitem__.assert_called_once_with('test_db')
        mock_mongo_client.return_value.__getitem__.return_value.__getitem__.assert_called_once_with('test_collection')
        assert mock_collection.insert_one.call_count == len(mock_root)

if __name__ == '__main__':
    unittest.main()