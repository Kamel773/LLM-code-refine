import unittest
from unittest.mock import patch, Mock
import xml.etree.ElementTree as ET

class TestXmlToCsv(unittest.TestCase):
    @patch('xml.etree.ElementTree.parse')
    @patch('pandas.DataFrame.to_csv')
    def test_xml_to_csv(self, mock_to_csv, mock_parse):
        mock_tree = Mock(spec=ET.ElementTree)
        mock_parse.return_value = mock_tree

        mock_root = Mock(spec=ET.Element)
        mock_tree.getroot.return_value = mock_root

        mock_elem = Mock(spec=ET.Element)
        mock_root.__iter__.return_value = iter([mock_elem])

        xml_to_csv('test.xml', 'test.csv')

        mock_parse.assert_called_once_with('test.xml')
        mock_to_csv.assert_called_once_with('test.csv', index=False)

if __name__ == '__main__':
    unittest.main()