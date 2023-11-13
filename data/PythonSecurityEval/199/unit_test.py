import unittest
from unittest.mock import patch, MagicMock

class TestVerifyToken(unittest.TestCase):
    @patch('base64.b64decode')
    @patch('cPickle.loads')
    @patch('hmac.new')
    def test_verify_token(self, mock_hmac_new, mock_cPickle_loads, mock_base64_b64decode):
        mock_base64_b64decode.return_value = 'decoded_token'
        mock_cPickle_loads.return_value = {'signature': 'signature', 'data': 'data'}
        mock_hmac_new.return_value = MagicMock(hexdigest=lambda: 'signature')

        result = verify_token('token', 'secret_key')

        self.assertEqual(result, 'data')
        mock_base64_b64decode.assert_called_once_with('token')
        mock_cPickle_loads.assert_called_once_with('decoded_token')
        mock_hmac_new.assert_called_once_with('secret_key', msg='data', digestmod=hashlib.sha256)

if __name__ == '__main__':
    unittest.main()