import unittest
from unittest.mock import patch, mock_open
import xml.etree.ElementTree as ET
from my_module import get_user_locations  # assuming the function is in a file called my_module.py

class TestGetUserLocations(unittest.TestCase):
    @patch('xml.etree.ElementTree.parse')
    def test_get_user_locations(self, mock_parse):
        mock_tree = ET.ElementTree(ET.Element('data'))
        mock_root = mock_tree.getroot()
        mock_user = ET.SubElement(mock_root, 'user', {'name': 'testuser'})
        ET.SubElement(mock_user, 'location').text = 'testlocation'
        mock_parse.return_value = mock_tree

        locations = get_user_locations('testuser', 'test.xml')
        self.assertEqual(locations, ['testlocation'])

if __name__ == '__main__':
    unittest.main()