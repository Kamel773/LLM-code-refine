import unittest
from unittest.mock import patch
from your_module import extract_ip_address  # replace 'your_module' with the name of your module

class TestExtractIpAddress(unittest.TestCase):
    @patch('your_module.re.findall')  # replace 'your_module' with the name of your module
    def test_extract_ip_address(self, mock_findall):
        mock_findall.return_value = ['192.168.1.1']
        result = extract_ip_address('The IP address is 192.168.1.1')
        self.assertEqual(result, ['192.168.1.1'])
        mock_findall.assert_called_once_with(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', 'The IP address is 192.168.1.1')

if __name__ == '__main__':
    unittest.main()