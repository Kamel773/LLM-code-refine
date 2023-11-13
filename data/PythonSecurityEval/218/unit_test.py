import unittest
from unittest.mock import patch, mock_open
from your_flask_app import app  # replace with your actual Flask app import

class TestDownload(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('flask.send_file', return_value='File sent')
    def test_download_file(self, mock_send_file):
        response = self.app.get('/download/test.txt')
        mock_send_file.assert_called_once_with('test.txt', as_attachment=True)
        self.assertEqual(response.data, b'File sent')

if __name__ == '__main__':
    unittest.main()