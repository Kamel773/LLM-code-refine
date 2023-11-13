import unittest
from unittest.mock import patch, mock_open
import xml.etree.ElementTree as ET
from my_module import get_root_element  # assuming the function is in a file called my_module.py

class TestGetRootElement(unittest.TestCase):
    @patch("xml.etree.ElementTree.parse")
    def test_get_root_element(self, mock_parse):
        mock_root = ET.Element("root")
        mock_tree = ET.ElementTree(mock_root)
        mock_parse.return_value = mock_tree

        with patch("builtins.open", mock_open(read_data="<root></root>")) as mock_file:
            result = get_root_element("dummy.xml")
            self.assertEqual(result, mock_root)

if __name__ == "__main__":
    unittest.main()