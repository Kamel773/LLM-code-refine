from unittest.mock import Mock, call

class TestSelectWithCondition(unittest.TestCase):
    def test_select_with_condition(self):
        # Set up the mock connection and cursor
        mock_con = Mock(sqlite3.Connection)
        mock_cur = Mock(sqlite3.Cursor)
        mock_con.cursor.return_value = mock_cur
        # Set up the mock for sqlite3.connect
        sqlite3.connect = Mock(return_value=mock_con)
        
        # Test the function
        condition = 'id = 1'
        select_with_condition('test.db', 'test_table', condition)
        
        # Check the mock calls
        sqlite3.connect.assert_called_once_with('test.db')
        mock_con.cursor.assert_called_once()
        query = f'SELECT * FROM test_table WHERE {condition}'
        mock_cur.execute.assert_called_once_with(query)
        mock_cur.fetchall.assert_called_once()
        mock_con.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()