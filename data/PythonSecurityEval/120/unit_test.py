import unittest
from unittest.mock import patch, Mock
import xml.etree.ElementTree as ET

class TestGetRoot(unittest.TestCase):
    @patch('xml.etree.ElementTree.fromstring')
    def test_get_root(self, mock_fromstring):
        mock_root = Mock()
        mock_fromstring.return_value = mock_root

        xml_string = '<root><child>text</child></root>'
        result = get_root(xml_string)

        mock_fromstring.assert_called_once_with(xml_string)
        self.assertEqual(result, mock_root)

if __name__ == '__main__':
    unittest.main()