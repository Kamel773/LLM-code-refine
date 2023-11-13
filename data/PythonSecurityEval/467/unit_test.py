import unittest
from unittest.mock import patch
from my_module import validate_ip

class TestValidateIP(unittest.TestCase):
    @patch('my_module.re.match')
    def test_validate_ip(self, mock_re):
        mock_re.return_value = True
        result = validate_ip('192.168.1.1')
        self.assertTrue(result)
        mock_re.assert_called_once_with(
            r"^"
            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
            r"$", 
            '192.168.1.1'
        )

if __name__ == '__main__':
    unittest.main()