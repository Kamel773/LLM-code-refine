import unittest
from unittest.mock import patch, mock_open

class TestCreateAndExecuteFile(unittest.TestCase):
    @patch('subprocess.run')
    @patch('os.chmod')
    @patch('builtins.open', new_callable=mock_open, read_data="#!/bin/bash\necho 'Hello, World!'")
    def test_create_and_execute_file(self, mock_file, mock_chmod, mock_run):
        mock_run.return_value.stdout = b'Hello, World!'
        result = create_and_execute_file()
        self.assertEqual(result, 'Hello, World!')

if __name__ == '__main__':
    unittest.main()