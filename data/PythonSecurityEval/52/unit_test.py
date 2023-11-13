import unittest
from unittest.mock import mock_open, patch
import xml.etree.cElementTree as ET

class TestParseXml(unittest.TestCase):
    def test_parse_xml(self):
        mock_data = """<?xml version="1.0"?>
                       <root>
                           <element>Text</element>
                       </root>"""
        
        with patch("builtins.open", mock_open(read_data=mock_data)):
            tree = parse_xml("file.xml")

        # Verify the XML was parsed correctly
        root = tree.getroot()
        self.assertEqual(root.tag, "root")
        self.assertEqual(root[0].tag, "element")
        self.assertEqual(root[0].text, "Text")

if __name__ == '__main__':
    unittest.main()
