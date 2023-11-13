import unittest
from unittest.mock import patch
from flask import json
from your_flask_app import app, db, User  # replace 'your_flask_app' with the name of your Flask app module

class TestCreateUser(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @patch('your_flask_app.db.session.commit')  # replace 'your_flask_app' with the name of your Flask app module
    def test_create_user(self, mock_db_commit):
        mock_db_commit.return_value = None
        response = self.client.post('/users', data=json.dumps({'name': 'John', 'email': 'john@example.com'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data), {'message': 'User created successfully!'})

if __name__ == '__main__':
    unittest.main()