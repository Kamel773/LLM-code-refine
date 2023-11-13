import unittest
from unittest.mock import patch
from your_flask_app_file import create_app

class TestApp(unittest.TestCase):

    @patch('flask_sqlalchemy.SQLAlchemy')
    def test_create_app(self, mock_sqlalchemy):
        app, db = create_app()
        self.assertEqual(app.config['SQLALCHEMY_DATABASE_URI'], 'sqlite:////tmp/test.db')
        mock_sqlalchemy.assert_called_once_with(app)

if __name__ == "__main__":
    unittest.main()