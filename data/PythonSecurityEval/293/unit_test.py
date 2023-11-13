import unittest
from unittest.mock import patch
from flask import request

class TestGenerateTokenAndStoreInCookie(unittest.TestCase):
    @patch('secrets.token_hex', return_value='mock_token')
    def test_generate_token_and_store_in_cookie(self, mock_token_hex):
        with app.test_request_context():
            resp = generate_token_and_store_in_cookie()
            self.assertEqual(request.cookies.get('session_token'), 'mock_token')

if __name__ == '__main__':
    unittest.main()