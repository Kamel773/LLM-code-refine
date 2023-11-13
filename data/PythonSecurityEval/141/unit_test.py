import unittest
from unittest.mock import patch, Mock
import importlib

class TestDynamicImport(unittest.TestCase):

    @patch('importlib.import_module')
    def test_import_module_dynamically(self, mock_import):
        # Arrange
        module_name = 'math'
        mock_module = Mock()
        mock_import.return_value = mock_module

        # Act
        result = import_module_dynamically(module_name)

        # Assert
        mock_import.assert_called_once_with(module_name)
        self.assertEqual(result, mock_module)

    @patch('importlib.import_module')
    def test_import_module_dynamically_not_found(self, mock_import):
        # Arrange
        module_name = 'non_existent_module'
        mock_import.side_effect = ImportError

        # Act
        result = import_module_dynamically(module_name)

        # Assert
        mock_import.assert_called_once_with(module_name)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()