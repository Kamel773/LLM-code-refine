import unittest
from unittest.mock import patch
import os
import your_module  # replace with the name of your module

class TestExecuteCommand(unittest.TestCase):
    @patch('your_module.os.system')  # replace with the name of your module
    @patch('your_module.input')  # replace with the name of your module
    def test_execute_command(self, input_mock, os_system_mock):
        # Arrange
        input_mock.return_value = 'ls'

        # Act
        your_module.execute_command()  # replace with the name of your module

        # Assert
        os_system_mock.assert_called_once_with('ls')

if __name__ == '__main__':
    unittest.main()