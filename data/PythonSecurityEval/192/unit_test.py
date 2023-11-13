import unittest
from unittest.mock import patch, mock_open
from werkzeug.datastructures import FileStorage
from your_flask_app import app, allowed_file

class UploadFileTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('werkzeug.datastructures.FileStorage.save')
    def test_upload_file(self, mock_save):
        data = {
            'file': (BytesIO(b'my file contents'), 'test.pdf')
        }
        response = self.app.post('/upload', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 302)
        self.assertTrue('/pdf/view' in response.location)
        mock_save.assert_called_once()

    def test_allowed_file(self):
        self.assertTrue(allowed_file('test.pdf'))
        self.assertFalse(allowed_file('test.exe'))

if __name__ == '__main__':
    unittest.main()