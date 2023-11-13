import unittest
from unittest.mock import patch, Mock
import your_script  # replace with the name of your script

class TestLoadJsonFromUrl(unittest.TestCase):
    @patch('requests.get')
    def test_load_json_from_url(self, mock_get):
        mock_response = Mock()
        mock_response.text = '{"key": "value"}'
        mock_get.return_value = mock_response

        data = your_script.load_json_from_url('http://example.com/data.json')
        self.assertEqual(data, {"key": "value"})

if __name__ == "__main__":
    unittest.main()