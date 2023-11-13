import unittest
from unittest.mock import patch, MagicMock
from myapp import app

class TestGetUser(unittest.TestCase):
    @patch('myapp.mysql')
    def test_get_user(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_mysql.connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = {'id': '1', 'data': 'test data'}

        tester = app.test_client(self)
        response = tester.get('/user/1', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'id': '1', 'data': 'test data'})

if __name__ == '__main__':
    unittest.main()