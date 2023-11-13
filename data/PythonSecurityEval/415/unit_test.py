import unittest
from unittest.mock import patch, MagicMock
from flask import json
from your_flask_app import app, db, Data  # replace 'your_flask_app' with the name of your Flask app file

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @patch('your_flask_app.db.session.add', return_value=None)  # replace 'your_flask_app' with the name of your Flask app file
    @patch('your_flask_app.db.session.commit', return_value=None)  # replace 'your_flask_app' with the name of your Flask app file
    def test_upload_file(self, mock_add, mock_commit):
        response = self.client.post('/upload', data=json.dumps({'key': 'value'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'message' : 'Data stored in database!'})

if __name__ == '__main__':
    unittest.main()