import unittest
from unittest.mock import patch, mock_open
import your_module  # replace with the name of the module where `load_module_from_path` is defined

class TestLoadModuleFromPath(unittest.TestCase):
    @patch('importlib.util.spec_from_file_location')
    @patch('importlib.util.module_from_spec')
    def test_load_module_from_path(self, mock_module_from_spec, mock_spec_from_file_location):
        mock_module = mock_module_from_spec.return_value
        mock_spec = mock_spec_from_file_location.return_value

        path = "/path/to/module.py"
        result = your_module.load_module_from_path(path)

        mock_spec_from_file_location.assert_called_once_with("module.name", path)
        mock_module_from_spec.assert_called_once_with(mock_spec)
        self.assertEqual(result, mock_module)

if __name__ == '__main__':
    unittest.main()