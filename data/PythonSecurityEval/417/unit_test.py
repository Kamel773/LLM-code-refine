import unittest
from unittest.mock import patch, Mock
from your_flask_app import app, db, Data

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @patch('pandas.read_csv')
    @patch('flask.request')
    def test_upload_file(self, mock_request, mock_read_csv):
        mock_file = Mock()
        mock_file.read.return_value.decode.return_value = 'data'
        mock_request.files = {'file': mock_file}
        mock_read_csv.return_value.iterrows.return_value = [('index', 'row')]

        response = self.app.post('/upload')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Success')
        self.assertEqual(Data.query.count(), 1)

if __name__ == '__main__':
    unittest.main()