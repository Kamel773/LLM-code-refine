import unittest
from unittest.mock import mock_open, patch

class TestXMLParser(unittest.TestCase):
    def test_parse_xml_to_tree(self):
        mock_data = """<root>
                         <child>Content</child>
                       </root>"""

        with patch("builtins.open", mock_open(read_data=mock_data), create=True) as mock_file:
            result = parse_xml_to_tree('mock_file.xml')

        mock_file.assert_called_once_with('mock_file.xml')

        self.assertIsNotNone(result)
        self.assertEqual(result.getroot().tag, 'root')

    def test_parse_xml_to_tree_file_not_found(self):
        with patch("builtins.open", mock_open(), create=True) as mock_file:
            mock_file.side_effect = FileNotFoundError
            result = parse_xml_to_tree('mock_file.xml')

        mock_file.assert_called_once_with('mock_file.xml')

        self.assertIsNone(result)

    def test_parse_xml_to_tree_invalid_xml(self):
        mock_data = """This is not a valid XML file."""

        with patch("builtins.open", mock_open(read_data=mock_data), create=True) as mock_file:
            result = parse_xml_to_tree('mock_file.xml')

        mock_file.assert_called_once_with('mock_file.xml')

        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
