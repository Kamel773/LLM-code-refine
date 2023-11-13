import unittest
from unittest.mock import patch, mock_open

class TestSaveImageToDB(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data=b"image_data")
    @patch('sqlite3.connect')
    def test_save_image_to_db(self, mock_sql_connect, mock_file_open):
        mock_conn = mock_sql_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        save_image_to_db("dummy_path")

        mock_file_open.assert_called_once_with("dummy_path", 'rb')
        mock_cursor.execute.assert_called_once_with("INSERT INTO images (data) VALUES (?)", (sqlite3.Binary(b"image_data"),))
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
