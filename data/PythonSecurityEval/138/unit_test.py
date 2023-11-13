import unittest
from unittest.mock import patch, Mock
import ldap3

class TestLdap(unittest.TestCase):
    @patch('ldap3.Server')
    @patch('ldap3.Connection')
    def test_search_user_in_ldap(self, mock_connection, mock_server):
        mock_conn_instance = Mock()
        mock_connection.return_value = mock_conn_instance
        mock_server_instance = Mock()
        mock_server.return_value = mock_server_instance

        server_name = 'my_server'
        username = 'my_username'
        password = 'my_password'
        search_base = 'ou=users,dc=example,dc=com'
        search_filter = '(objectClass=person)'

        result = search_user_in_ldap(server_name, username, password, search_base, search_filter)

        mock_server.assert_called_once_with(server_name, get_info=ldap3.ALL)
        mock_connection.assert_called_once_with(mock_server_instance, username, password, auto_bind=True)
        mock_conn_instance.search.assert_called_once_with(search_base, search_filter)
        self.assertEqual(result, mock_conn_instance.entries)

if __name__ == '__main__':
    unittest.main()