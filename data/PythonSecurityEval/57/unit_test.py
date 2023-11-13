from unittest import mock
import xml.etree.ElementTree as ET

class TestReadXML(unittest.TestCase):
    @mock.patch('xml.etree.ElementTree.parse')
    def test_read_xml_document(self, mock_parse):
        # Define the mock return value
        mock_tree = ET.ElementTree(ET.Element('root'))
        mock_parse.return_value = mock_tree

        # Call the function with a mock filepath
        result = read_xml_document('mock_file.xml')

        # Check the function used the mock return value
        self.assertEqual(result, mock_tree)

        # Check that the function called parse() with the correct argument
        mock_parse.assert_called_once_with('mock_file.xml')

if __name__ == '__main__':
    unittest.main()
