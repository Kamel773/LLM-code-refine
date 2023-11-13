import unittest
from unittest.mock import patch, Mock

class TestGetSingleResult(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_get_single_result(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = ('expected_result',)

        query = 'SELECT * FROM my_table'
        result = get_single_result(query)
        
        mock_connect.assert_called_once_with('my_database.db')
        mock_cursor.execute.assert_called_once_with(query)
        mock_cursor.fetchone.assert_called_once()

        self.assertEqual(result, ('expected_result',))

if __name__ == '__main__':
    unittest.main()
