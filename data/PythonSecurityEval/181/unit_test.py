import unittest
from unittest.mock import patch, Mock
import jwt

class TestVerifyDecodeJwt(unittest.TestCase):
    @patch('jwt.decode')
    def test_verify_decode_jwt(self, mock_decode):
        # Arrange
        test_token = 'test_token'
        test_secret_key = 'test_secret_key'
        test_payload = {'user_id': 1, 'username': 'test_user'}
        mock_decode.return_value = test_payload

        # Act
        result = verify_decode_jwt(test_token, test_secret_key)

        # Assert
        mock_decode.assert_called_once_with(test_token, test_secret_key, algorithms=["HS256"])
        self.assertEqual(result, test_payload)

if __name__ == '__main__':
    unittest.main()