import unittest
from unittest.mock import patch, Mock
from my_flask_app import app  # replace with the name of your Flask app module

class TestQueryRecords(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_query_records(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('record1', 'record2')]

        response = app.test_client().get('/query?q=SELECT * FROM my_table')

        mock_connect.assert_called_once_with('my_database.db')
        mock_cursor.execute.assert_called_once_with('SELECT * FROM my_table')
        self.assertEqual(response.get_json(), {'results': [('record1', 'record2')]})

if __name__ == '__main__':
    unittest.main()