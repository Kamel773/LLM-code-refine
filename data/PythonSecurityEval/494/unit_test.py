import unittest
from app import app, db, User

class TestRegister(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db
        self.db.create_all()

    def tearDown(self):
        User.query.delete()
        self.db.session.commit()

    def test_register(self):
        response = self.app.post('/register', data=dict(
            username='test',
            password='test'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        user = User.query.filter_by(username='test').first()
        self.assertIsNotNone(user)
        self.assertTrue(user.check_password('test'))

if __name__ == '__main__':
    unittest.main()