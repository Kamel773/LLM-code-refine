import unittest
from unittest.mock import patch
import jwt

class TestVerifyJwt(unittest.TestCase):
    @patch('jwt.decode')
    def test_verify_jwt(self, mock_decode):
        mock_decode.return_value = {'user_id': 1}

        token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxfQ.I-lVqIuKzGItgP2GnYMy3O8ePjZxRVQZ_x4gDZ89rus'
        secret = 'secret'

        result = verify_jwt(token, secret)

        self.assertEqual(result, {'user_id': 1})
        mock_decode.assert_called_once_with(token, secret, algorithms=['HS256'])

if __name__ == '__main__':
    unittest.main()