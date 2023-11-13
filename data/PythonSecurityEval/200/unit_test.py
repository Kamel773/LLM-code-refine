import unittest
from unittest.mock import patch, Mock
import yaml

class TestLoadYamlFromRequest(unittest.TestCase):
    @patch('requests.get')
    def test_load_yaml_from_request(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = """
        - just: 
          - a
          - simple
          - yaml
        """
        mock_get.return_value = mock_response

        expected_data = [{'just': ['a', 'simple', 'yaml']}]
        url = 'http://example.com/data.yaml'
        data = load_yaml_from_request(url)
        self.assertEqual(data, expected_data)

if __name__ == '__main__':
    unittest.main()