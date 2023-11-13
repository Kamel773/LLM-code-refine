import unittest
from unittest.mock import mock_open, patch
import xml.etree.ElementTree as ET

class TestExtractElements(unittest.TestCase):
    @patch('xml.etree.ElementTree.parse')
    def test_extract_elements(self, mock_parse):
        mock_tree = ET.ElementTree(ET.Element('root'))
        mock_root = mock_tree.getroot()
        ET.SubElement(mock_root, 'name').text = 'John'
        ET.SubElement(mock_root, 'name').text = 'Doe'
        mock_parse.return_value = mock_tree

        names = extract_elements('dummy_file_path')
        self.assertEqual(names, ['John', 'Doe'])

if __name__ == '__main__':
    unittest.main()