import unittest
from unittest.mock import patch, Mock

class TestOrderByCondition(unittest.TestCase):

    @patch('sqlite3.connect')
    def test_order_by_condition(self, mock_sqlite3_connect):
        mock_conn = Mock()
        mock_sqlite3_connect.return_value = mock_conn
        mock_cursor = Mock()
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('mocked_data',)]

        db_path = 'test.db'
        table_name = 'test_table'
        condition = 'column1 > 10'
        order = 'column2 DESC'

        expected_data = [('mocked_data',)]
        returned_data = order_by_condition(db_path, table_name, condition, order)

        self.assertEqual(returned_data, expected_data)
        mock_sqlite3_connect.assert_called_once_with(db_path)
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(f"SELECT * FROM {table_name} WHERE {condition} ORDER BY {order};")
        mock_cursor.fetchall.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
