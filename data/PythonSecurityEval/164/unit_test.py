import unittest
from unittest.mock import patch, MagicMock
import ssl

class TestSSLContext(unittest.TestCase):
    @patch('ssl.SSLContext')
    def test_create_ssl_context(self, mock_ssl_context):
        from your_module import create_ssl_context  # replace 'your_module' with the name of your module

        mock_context = MagicMock()
        mock_ssl_context.return_value = mock_context

        result = create_ssl_context()

        mock_ssl_context.assert_called_once_with(ssl.PROTOCOL_TLSv1_2)
        self.assertEqual(result, mock_context)

if __name__ == '__main__':
    unittest.main()