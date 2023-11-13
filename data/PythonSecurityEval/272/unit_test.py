import unittest
from unittest.mock import patch, MagicMock

class TestCreateTable(unittest.TestCase):
    @patch('psycopg2.connect')
    def test_create_table(self, mock_connect):
        # Arrange
        mock_conn = mock_connect.return_value
        mock_cur = mock_conn.cursor.return_value

        # Act
        result = create_table('test_db', 'test_user', 'test_password', 'test_table')

        # Assert
        self.assertTrue(result)
        mock_connect.assert_called_once_with(dbname='test_db', user='test_user', password='test_password')
        mock_cur.execute.assert_called_once()
        mock_conn.commit.assert_called_once()
        mock_cur.close.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()