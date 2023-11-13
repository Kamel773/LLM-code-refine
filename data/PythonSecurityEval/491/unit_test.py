import unittest
from unittest.mock import mock_open, patch
import my_module  # replace this with the name of the module where you defined the function above

class TestReadPasswordFromConfig(unittest.TestCase):
    @patch('my_module.json.load')
    @patch('my_module.open', new_callable=mock_open, read_data='{"password": "secret"}')
    def test_read_password_from_config(self, mock_open, mock_json):
        mock_json.return_value = {'password': 'secret'}
        result = my_module.read_password_from_config('fake_path')
        self.assertEqual(result, 'secret')
        mock_open.assert_called_once_with('fake_path', 'r')
        mock_json.assert_called_once()

if __name__ == '__main__':
    unittest.main()