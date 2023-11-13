import unittest
from unittest.mock import patch, mock_open
import xml.etree.ElementTree as ET

class TestAddElementToXml(unittest.TestCase):
    @patch('xml.etree.ElementTree.parse')
    @patch('xml.etree.ElementTree.Element')
    @patch('builtins.open', new_callable=mock_open)
    def test_add_element_to_xml(self, mock_file, mock_element, mock_parse):
        # Mock the XML tree and root
        mock_tree = mock_parse.return_value
        mock_root = mock_tree.getroot.return_value

        # Call the function with the mock objects
        add_element_to_xml('mock_file.xml', 'new_element', 1)

        # Assert that the new element was created
        mock_element.assert_called_once_with('new_element')

        # Assert that the new element was inserted at the correct location
        mock_root.insert.assert_called_once_with(1, mock_element.return_value)

        # Assert that the changes were written back to the file
        mock_tree.write.assert_called_once_with('mock_file.xml')

if __name__ == '__main__':
    unittest.main()