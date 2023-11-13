import unittest
from unittest.mock import patch

class TestExtractTextFromXML(unittest.TestCase):

    @patch('xml.etree.ElementTree.fromstring')
    def test_extract_text_from_xml(self, mock_fromstring):
        mock_root = mock_fromstring.return_value
        mock_root.itertext.return_value = ['Hello', ' ', 'World']
        xml_string = '<root><child>Hello</child> <child>World</child></root>'
        result = extract_text_from_xml(xml_string)
        self.assertEqual(result, 'Hello World')

if __name__ == '__main__':
    unittest.main()