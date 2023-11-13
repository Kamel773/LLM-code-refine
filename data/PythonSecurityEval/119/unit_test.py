import unittest
from unittest.mock import patch, mock_open
import yaml

class TestLoadYamlFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="key: value")
    @patch('yaml.safe_load')
    def test_load_yaml_file(self, mock_safe_load, mock_open):
        mock_safe_load.return_value = {'key': 'value'}
        
        from my_module import load_yaml_file  # assuming the function is in my_module.py
        result = load_yaml_file('fake_path')

        mock_open.assert_called_once_with('fake_path', 'r')
        mock_safe_load.assert_called_once()
        self.assertEqual(result, {'key': 'value'})

if __name__ == '__main__':
    unittest.main()