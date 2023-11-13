import unittest
from unittest.mock import patch, mock_open
from cryptography.fernet import Fernet
import your_module  # replace with your actual module name

class TestEncryption(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="secret_key")
    def test_encrypt_message(self, mock_open):
        with patch.object(Fernet, "encrypt", return_value="encrypted_message") as mock_encrypt:
            result = your_module.encrypt_message("test_message")
            self.assertEqual(result, "encrypted_message")
            mock_encrypt.assert_called_once_with("test_message".encode())

if __name__ == "__main__":
    unittest.main()