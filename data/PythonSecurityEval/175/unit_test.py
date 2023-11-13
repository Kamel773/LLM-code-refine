import unittest
from unittest.mock import patch, mock_open
import your_module  # replace with the name of the module where check_certificate is defined

class TestCheckCertificate(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="test certificate")
    def test_check_certificate(self, mock_file):
        known_hash = hashlib.sha256("test certificate".encode()).hexdigest()
        self.assertTrue(your_module.check_certificate("test certificate", known_hash))

    @patch("builtins.open", new_callable=mock_open, read_data="test certificate")
    def test_check_certificate_fail(self, mock_file):
        known_hash = hashlib.sha256("wrong certificate".encode()).hexdigest()
        self.assertFalse(your_module.check_certificate("test certificate", known_hash))

if __name__ == '__main__':
    unittest.main()