import unittest
from unittest.mock import patch, mock_open
import xml.etree.ElementTree as ET
from my_module import xml_to_dict  # replace with the actual module name

class TestXmlToDict(unittest.TestCase):
    @patch('xml.etree.ElementTree.parse')
    def test_xml_to_dict(self, mock_parse):
        mock_root = ET.Element('root')
        mock_child1 = ET.SubElement(mock_root, 'child1')
        mock_child1.text = 'text1'
        mock_child2 = ET.SubElement(mock_root, 'child2')
        mock_child2.text = 'text2'
        mock_tree = ET.ElementTree(mock_root)
        mock_parse.return_value = mock_tree

        expected_dict = {'root': {'child1': 'text1', 'child2': 'text2'}}
        with patch('builtins.open', new_callable=mock_open) as mock_file:
            result_dict = xml_to_dict('mock_file.xml')
        self.assertEqual(result_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()