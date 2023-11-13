import unittest
from unittest.mock import patch

class TestSensitiveData(unittest.TestCase):
    @patch('__main__.sensitive_data', create=True)
    def test_store_sensitive_data(self, mock_sensitive_data):
        data = "secret_password"
        store_sensitive_data(data)
        self.assertEqual(mock_sensitive_data, data)

if __name__ == '__main__':
    unittest.main()