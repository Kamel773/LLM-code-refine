import subprocess
import unittest
from unittest.mock import patch

class TestCallScript(unittest.TestCase):
    @patch('subprocess.run')
    def test_run_script_with_args(self, mock_run):
        script_path = "script_to_run.py"
        args = ["arg1", "arg2", "arg3"]
        run_script_with_args(script_path, args)

        # check that subprocess.run was called with the correct arguments
        mock_run.assert_called_once_with(["python3", script_path] + args, check=True)

if __name__ == "__main__":
    unittest.main()  # Run the unit test