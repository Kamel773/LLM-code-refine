import unittest
from unittest.mock import patch, MagicMock

class TestFilterXML(unittest.TestCase):
    @patch('lxml.etree.fromstring')
    @patch('lxml.etree.tostring')
    def test_filter_xml(self, mock_tostring, mock_fromstring):
        # Set up the mock objects
        mock_el = MagicMock()
        mock_tree = MagicMock()
        mock_tree.xpath.return_value = [mock_el]

        mock_fromstring.return_value = mock_tree
        mock_tostring.return_value = b'<mock>xml</mock>'

        # Run the function with a mock XML string and XPath query
        xml_string = '<root><child>value</child></root>'
        xpath_query = '//child'
        result = filter_xml(xml_string, xpath_query)

        # Check that the function called the mock objects correctly
        mock_fromstring.assert_called_once_with(xml_string)
        mock_tree.xpath.assert_called_once_with(xpath_query)
        mock_tostring.assert_called_once_with(mock_el, pretty_print=True)

        # Check that the function returned the correct result
        self.assertEqual(result, ['<mock>xml</mock>'])

if __name__ == '__main__':
    unittest.main()