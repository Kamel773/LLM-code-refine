import unittest
from unittest.mock import patch, mock_open
import xml.etree.ElementTree as ET

class TestDictToXml(unittest.TestCase):
    @patch("xml.etree.ElementTree.ElementTree.write")
    def test_dict_to_xml(self, mock_write):
        mock_file = mock_open()
        with patch("builtins.open", mock_file):
            input_dict = {"key1": "value1", "key2": "value2"}
            dict_to_xml(input_dict, "output.xml")
            mock_file.assert_called_once_with("output.xml", "wb")
            mock_write.assert_called_once()

            # Create expected XML tree
            root = ET.Element("root")
            for key, value in input_dict.items():
                child = ET.SubElement(root, key)
                child.text = str(value)
            expected_tree = ET.ElementTree(root)

            # Compare actual and expected XML trees
            self.assertEqual(ET.tostring(expected_tree.getroot()), ET.tostring(mock_write.call_args[0][0].getroot()))

if __name__ == "__main__":
    unittest.main()