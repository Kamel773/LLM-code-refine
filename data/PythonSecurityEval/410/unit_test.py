import unittest
from unittest.mock import patch, mock_open
import psycopg2
import psycopg2.extras
import your_module  # replace with the name of the module where you defined the above function

class TestStoreVideoFile(unittest.TestCase):
    @patch('your_module.psycopg2.connect')
    @patch('your_module.open', new_callable=mock_open, read_data=b'video data')
    def test_store_video_file(self, mock_file, mock_db):
        mock_cursor = mock_db.return_value.cursor.return_value

        your_module.store_video_file('path/to/video')

        mock_file.assert_called_once_with('path/to/video', 'rb')
        mock_db.assert_called_once_with("dbname=test user=postgres password=secret")
        mock_cursor.execute.assert_called_once_with("INSERT INTO video_table (video_column) VALUES (%s)", (psycopg2.Binary(b'video data'),))
        mock_db.return_value.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()