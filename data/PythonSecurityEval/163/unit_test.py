import unittest
from unittest.mock import patch, MagicMock
import ssl

class TestSSLContext(unittest.TestCase):
    @patch('ssl.create_default_context')
    def test_create_unverified_ssl_context(self, mock_create_default_context):
        mock_context = MagicMock()
        mock_create_default_context.return_value = mock_context

        from your_module import create_unverified_ssl_context
        context = create_unverified_ssl_context()

        self.assertEqual(context, mock_context)
        self.assertFalse(context.check_hostname)
        self.assertEqual(context.verify_mode, ssl.CERT_NONE)

if __name__ == '__main__':
    unittest.main()