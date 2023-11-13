from unittest.mock import patch, Mock
import xml.etree.ElementTree as ET

class TestAddElementToXML(unittest.TestCase):
    @patch('xml.etree.ElementTree.parse')
    @patch('xml.etree.ElementTree.ElementTree.write')
    def test_add_element_to_xml(self, mock_write, mock_parse):
        mock_tree = Mock()
        mock_root = Mock()
        
        mock_tree.getroot.return_value = mock_root
        mock_parse.return_value = mock_tree

        file_path = 'mock_file.xml'
        new_element = 'new_elem'
        element_text = 'some text'
        
        add_element_to_xml(file_path, new_element, element_text)
        
        # Test if parse is called with correct file path
        mock_parse.assert_called_once_with(file_path)
        
        # Test if SubElement is called with correct parameters
        ET.SubElement.assert_called_once_with(mock_root, new_element)
        
        # Test if write is called with correct file path
        mock_write.assert_called_once_with(file_path)


if __name__ == '__main__':
    unittest.main()
