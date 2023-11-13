import unittest
from unittest.mock import patch, Mock
import xml.etree.ElementTree as ET

class TestExtractTextFromXml(unittest.TestCase):
    @patch('xml.etree.ElementTree.fromstring')
    def test_extract_text_from_xml(self, mock_fromstring):
        mock_root = Mock()
        mock_root.itertext.return_value = ['Hello', ' ', 'World']
        mock_fromstring.return_value = mock_root

        xml_string = '<root>Hello World</root>'
        result = extract_text_from_xml(xml_string)

        self.assertEqual(result, 'Hello World')
        mock_fromstring.assert_called_once_with(xml_string)
        mock_root.itertext.assert_called_once()

if __name__ == '__main__':
    unittest.main()