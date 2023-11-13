import unittest
from unittest.mock import patch, mock_open
import xml.etree.ElementTree as ET
from my_module import parse_xml  # assuming the function is in a file named my_module.py

class TestParseXml(unittest.TestCase):
    @patch("xml.etree.ElementTree.parse")
    def test_parse_xml(self, mock_parse):
        mock_root = ET.Element("root")
        mock_tree = ET.ElementTree(mock_root)
        mock_parse.return_value = mock_tree

        with patch("builtins.open", mock_open(read_data="<root></root>")) as mock_file:
            result = parse_xml("dummy_file.xml")
            mock_file.assert_called_once_with("dummy_file.xml")
            mock_parse.assert_called_once_with("dummy_file.xml")
            self.assertEqual(result, mock_root)

if __name__ == "__main__":
    unittest.main()