import unittest
from unittest.mock import patch, MagicMock
from my_module import generate_dsa_private_key

class TestGenerateDSAPrivateKey(unittest.TestCase):
    @patch('my_module.dsa.generate_private_key')
    @patch('my_module.default_backend')
    def test_generate_dsa_private_key(self, mock_backend, mock_generate_private_key):
        mock_key = MagicMock()
        mock_key.private_bytes.return_value = b'test_key'
        mock_generate_private_key.return_value = mock_key

        result = generate_dsa_private_key()

        mock_generate_private_key.assert_called_once_with(key_size=2048, backend=mock_backend())
        mock_key.private_bytes.assert_called_once_with(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        self.assertEqual(result, 'test_key')

if __name__ == '__main__':
    unittest.main()