import unittest
from unittest.mock import patch
import your_module  # replace with the name of the module where you defined the generate_token function

class TestGenerateToken(unittest.TestCase):
    @patch('secrets.token_hex')
    def test_generate_token(self, mock_token_hex):
        mock_token_hex.return_value = 'test_token'
        result = your_module.generate_token()
        self.assertEqual(result, 'test_token')
        mock_token_hex.assert_called_once_with(16)

if __name__ == '__main__':
    unittest.main()