import unittest
from unittest.mock import patch, Mock
from your_module import test_db_connection  # Adjust the import based on where your function is located

class TestDBConnection(unittest.TestCase):

    @patch('your_module.connections')  # Adjust the path based on where your function is located
    def test_successful_db_connection(self, mock_connections):
        # Mocking a successful connection
        mock_cursor = Mock()
        mock_connections['default'].cursor.return_value = mock_cursor

        result = test_db_connection()
        self.assertTrue(result)

    @patch('your_module.connections')  # Adjust the path based on where your function is located
    def test_failed_db_connection(self, mock_connections):
        # Mocking a failed connection
        mock_connections['default'].cursor.side_effect = OperationalError

        result = test_db_connection()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
