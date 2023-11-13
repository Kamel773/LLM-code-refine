import unittest
from unittest.mock import patch, MagicMock
import mysql.connector
import your_module  # replace with the name of the module where get_all_rows is defined

class TestGetAllRows(unittest.TestCase):
    @patch.object(mysql.connector, 'connect')
    def test_get_all_rows(self, mock_connect):
        # Arrange
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('row1', 'row2')]

        # Act
        result = your_module.get_all_rows('test_db', 'test_table')

        # Assert
        mock_connect.assert_called_once_with(user='username', password='password', host='localhost', database='test_db')
        mock_cursor.execute.assert_called_once_with('SELECT * FROM test_table')
        self.assertEqual(result, [('row1', 'row2')])

if __name__ == '__main__':
    unittest.main()