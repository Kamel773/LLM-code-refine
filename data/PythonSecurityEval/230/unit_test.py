import unittest
from unittest.mock import patch
from flask import Flask
from your_flask_app import parse_xml  # replace with your actual Flask app module

class TestParseXML(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    @patch('your_flask_app.request')  # replace with your actual Flask app module
    def test_parse_xml(self, mock_request):
        mock_request.data = '<root><child>data</child></root>'.encode()
        response = parse_xml()
        self.assertEqual(response, ({'message': '<root><child>data</child></root>'}, 200))

    @patch('your_flask_app.request')  # replace with your actual Flask app module
    def test_parse_xml_invalid(self, mock_request):
        mock_request.data = 'invalid xml'.encode()
        response = parse_xml()
        self.assertEqual(response, ({'message': 'Invalid XML'}, 400))

if __name__ == '__main__':
    unittest.main()