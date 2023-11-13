import unittest
from unittest.mock import patch, call
import your_module  # replace with the name of the module where `execute_script` is defined

class TestExecuteScript(unittest.TestCase):
    @patch('subprocess.check_call')
    def test_execute_script(self, mock_check_call):
        # Test successful script execution
        script_path = "path/to/successful_script.py"
        self.assertTrue(your_module.execute_script(script_path))
        mock_check_call.assert_called_once_with(["python", script_path])

        # Test failed script execution
        mock_check_call.reset_mock()
        mock_check_call.side_effect = subprocess.CalledProcessError(1, 'cmd')
        script_path = "path/to/failed_script.py"
        self.assertFalse(your_module.execute_script(script_path))
        mock_check_call.assert_called_once_with(["python", script_path])

if __name__ == '__main__':
    unittest.main()