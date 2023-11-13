import unittest
from unittest.mock import patch, Mock

class TestInsertIntoTable(unittest.TestCase):

    @patch('sqlite3.connect')
    def test_insert_into_table(self, mock_connect):
        # Mock the connection and cursor
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Test data
        db_name = "test.db"
        table_name = "test_table"
        columns = ["id", "name"]
        data = [(1, "Alice"), (2, "Bob")]

        # Call the function
        insert_into_table(db_name, table_name, columns, data)

        # Assert that the correct SQL was executed
        mock_cursor.executemany.assert_called_once_with(
            "INSERT INTO test_table (id, name) VALUES (?, ?)", data
        )
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()
