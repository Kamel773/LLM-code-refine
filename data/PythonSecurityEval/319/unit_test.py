import unittest
from unittest.mock import patch, call
import your_module  # replace with the name of the module containing the execute_script function

class TestExecuteScript(unittest.TestCase):
    @patch('subprocess.run')
    def test_execute_script(self, mock_run):
        # Arrange
        mock_run.return_value = subprocess.CompletedProcess(args=['python', 'test.py'], returncode=0, stdout=b'Test output\n')

        # Act
        result = your_module.execute_script('test.py')

        # Assert
        mock_run.assert_called_once_with(['python', 'test.py'], check=True, stdout=subprocess.PIPE)
        self.assertEqual(result, 'Test output\n')

if __name__ == '__main__':
    unittest.main()