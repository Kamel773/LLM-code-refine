import unittest
from unittest.mock import patch, mock_open, MagicMock
from my_module import parse_xml_schema  # assuming the function is in my_module.py

class TestParseXmlSchema(unittest.TestCase):
    @patch('my_module.etree.XMLSchema')
    @patch('my_module.etree.parse')
    @patch('builtins.open', new_callable=mock_open, read_data='<xml></xml>')
    def test_parse_xml_schema(self, mock_open, mock_parse, mock_xmlschema):
        mock_parse.return_value = MagicMock()
        mock_xmlschema.return_value = MagicMock()

        result = parse_xml_schema('dummy_path')

        mock_open.assert_called_once_with('dummy_path', 'r')
        mock_parse.assert_called_once()
        mock_xmlschema.assert_called_once_with(mock_parse.return_value)
        self.assertEqual(result, mock_xmlschema.return_value)

if __name__ == '__main__':
    unittest.main()