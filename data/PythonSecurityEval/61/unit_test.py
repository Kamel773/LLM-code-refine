from unittest.mock import patch, MagicMock

class TestGetSubchildValue(unittest.TestCase):
    @patch('xml.dom.minidom.parseString')
    def test_get_subchild_value(self, mock_parse):
        # Create a MagicMock to return as the child node value
        mock_node_value = MagicMock()
        mock_node_value.nodeValue = 'mock value'
        
        # Setup the mock objects to return from parseString
        mock_child_node = MagicMock()
        mock_child_node.firstChild = mock_node_value
        mock_child_node.getElementsByTagName.return_value = [mock_child_node]
        
        mock_parent_node = MagicMock()
        mock_parent_node.getElementsByTagName.return_value = [mock_child_node]
        
        mock_parse.return_value.getElementsByTagName.return_value = [mock_parent_node]
        
        # Call the function
        value = get_subchild_value('<test><parent><child>value</child></parent></test>', 'parent', 'child')
        
        # Check the returned value
        self.assertEqual(value, 'mock value')

if __name__ == "__main__":
    unittest.main()
