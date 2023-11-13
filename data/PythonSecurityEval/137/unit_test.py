import unittest
from unittest.mock import patch, Mock
from flask import json
from your_flask_app import app  # replace with your actual Flask app import

class TestSearchUser(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('ldap.initialize')
    def test_search_user(self, mock_ldap):
        mock_conn = Mock()
        mock_ldap.return_value = mock_conn
        mock_conn.search_s.return_value = [('cn=test,dc=example,dc=com', {'sAMAccountName': [b'test']})]

        response = self.app.post('/search_user', data=json.dumps({'dc': 'example', 'username': 'test'}), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'result': [('cn=test,dc=example,dc=com', {'sAMAccountName': [b'test']})]})

if __name__ == '__main__':
    unittest.main()