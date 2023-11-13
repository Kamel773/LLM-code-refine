import unittest
from unittest.mock import patch

import json
import xmltodict
import unittest
from unittest.mock import patch, mock_open

def convert_xml_to_json(xml_file):
    with open(xml_file, 'r') as file:
        xml_content = file.read()
    json_content = json.dumps(xmltodict.parse(xml_content))
    return json_content

class TestConversion(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="<root><test>123</test></root>")
    def test_convert_xml_to_json(self, mock_file):
        expected_json = '{"root": {"test": "123"}}'
        result = convert_xml_to_json("dummy.xml")
        self.assertEqual(result, expected_json)

if __name__ == "__main__":
    unittest.main()