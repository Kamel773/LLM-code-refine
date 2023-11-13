import unittest
from unittest import mock
from my_module import verify_jwt_token

class TestVerifyJwtToken(unittest.TestCase):
    @mock.patch('jwt.decode')
    def test_verify_jwt_token(self, mock_decode):
        mock_decode.return_value = {'username': 'testuser'}
        result = verify_jwt_token('fake_token', 'fake_key')
        self.assertEqual(result, {'username': 'testuser'})
        mock_decode.assert_called_once_with('fake_token', 'fake_key', algorithms=['HS256'])

    @mock.patch('jwt.decode')
    def test_verify_jwt_token_expired(self, mock_decode):
        mock_decode.side_effect = jwt.ExpiredSignatureError
        result = verify_jwt_token('fake_token', 'fake_key')
        self.assertEqual(result, 'Signature expired. Please log in again.')

    @mock.patch('jwt.decode')
    def test_verify_jwt_token_invalid(self, mock_decode):
        mock_decode.side_effect = jwt.InvalidTokenError
        result = verify_jwt_token('fake_token', 'fake_key')
        self.assertEqual(result, 'Invalid token. Please log in again.')

if __name__ == '__main__':
    unittest.main()