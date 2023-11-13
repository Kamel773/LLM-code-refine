import unittest
from unittest.mock import patch, Mock
import your_module  # replace with the name of the module where you defined the function

class TestReadJsonFromUrl(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_read_json_from_url(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value.decode.return_value = '{"key": "value"}'
        result = your_module.read_json_from_url('https://example.com')
        self.assertEqual(result, {"key": "value"})

if __name__ == '__main__':
    unittest.main()