import unittest
from unittest.mock import Mock, patch

class TestConvertEtreeToString(unittest.TestCase):
    @patch('xml.etree.ElementTree.tostring')
    def test_convert_etree_to_string(self, mock_tostring):
        mock_etree = Mock()
        mock_tostring.return_value = b'<root><child>text</child></root>'

        result = convert_etree_to_string(mock_etree)

        mock_tostring.assert_called_once_with(mock_etree, encoding='utf8')
        self.assertEqual(result, '<root><child>text</child></root>')

if __name__ == '__main__':
    unittest.main()