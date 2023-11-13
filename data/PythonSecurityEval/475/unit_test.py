import unittest
from unittest.mock import patch
import your_module  # replace with the name of the module where you defined the function

class TestLoadAndExecuteScript(unittest.TestCase):
    @patch('requests.get')
    def test_load_and_execute_script(self, mock_get):
        mock_get.return_value.text = 'print("Hello, World!")'
        your_module.load_and_execute_script('http://example.com/script.py')
        mock_get.assert_called_once_with('http://example.com/script.py')

if __name__ == '__main__':
    unittest.main()