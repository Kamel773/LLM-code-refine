import unittest
from unittest.mock import patch

class TestSearchAndReplaceInXml(unittest.TestCase):
    @patch('xml.etree.ElementTree.parse')
    def test_search_and_replace_in_xml(self, mock_parse):
        mock_tree = ET.ElementTree(ET.Element('root'))
        mock_root = mock_tree.getroot()
        mock_elem = ET.SubElement(mock_root, 'element')
        mock_elem.text = 'old_text'

        mock_parse.return_value = mock_tree

        with patch('builtins.open', new=mock_open()) as mock_file:
            search_and_replace_in_xml('fake_path', 'old_text', 'new_text')

        self.assertEqual(mock_elem.text, 'new_text')

if __name__ == '__main__':
    unittest.main()