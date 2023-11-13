import unittest
from unittest.mock import patch, mock_open
from your_flask_app import upload_image

class TestUploadImage(unittest.TestCase):
    @patch('your_flask_app.secure_filename')
    @patch('your_flask_app.os.path.join')
    @patch('your_flask_app.open', new_callable=mock_open, read_data="image_data")
    def test_upload_image(self, mock_open, mock_join, mock_secure):
        mock_file = unittest.mock.Mock()
        mock_file.filename = 'test.jpg'
        mock_secure.return_value = 'test.jpg'
        mock_join.return_value = 'uploads/test.jpg'

        result = upload_image(mock_file, 'uploads/')

        self.assertEqual(result, 'uploads/test.jpg')
        mock_open.assert_called_with('uploads/test.jpg', 'w')
        mock_open().write.assert_called_with('aW1hZ2VfZGF0YQ==')

if __name__ == '__main__':
    unittest.main()