import unittest
from unittest.mock import patch, MagicMock

class TestXmlToPostgres(unittest.TestCase):
    @patch('psycopg2.connect')
    @patch('xml.etree.ElementTree.parse')
    def test_xml_to_postgres(self, mock_parse, mock_connect):
        # Mock XML data
        mock_tree = MagicMock()
        mock_root = MagicMock()
        mock_tree.getroot.return_value = mock_root
        mock_parse.return_value = mock_tree

        # Mock PostgreSQL connection
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_conn.cursor.return_value = mock_cur
        mock_connect.return_value = mock_conn

        xml_to_postgres('test.xml', 'test_db', 'test_user', 'test_password', 'localhost', '5432')

        # Check if functions were called with correct arguments
        mock_parse.assert_called_once_with('test.xml')
        mock_connect.assert_called_once_with(database='test_db', user='test_user', password='test_password', host='localhost', port='5432')

if __name__ == '__main__':
    unittest.main()