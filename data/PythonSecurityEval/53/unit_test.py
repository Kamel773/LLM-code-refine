import xml.etree.ElementTree as ET
import os
import unittest
from unittest.mock import patch, mock_open

class TestCreateXml(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    @patch("xml.etree.ElementTree.ElementTree.write")
    def test_create_xml(self, mock_write, mock_file):
        filename = "test.xml"
        root_element = "root"
        sub_elements = {"sub1": "text1", "sub2": "text2"}

        create_xml(filename, root_element, sub_elements)

        self.assertEqual(mock_write.call_count, 1)
        mock_write.assert_called_with(filename)

if __name__ == "__main__":
    unittest.main()