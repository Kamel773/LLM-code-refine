import unittest
from unittest import mock
from io import StringIO

class TestXmlToDict(unittest.TestCase):
    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data='<root><child>data</child></root>')
    def test_xml_to_dict(self, mock_open):
        expected_dict = {'root': {'child': 'data'}}
        result = xml_to_dict('fake_path')
        self.assertEqual(result, expected_dict)

if __name__ == '__main__':
    unittest.main()