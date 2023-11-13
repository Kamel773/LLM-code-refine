import unittest
from unittest.mock import patch
from command_dispatcher import CommandDispatcher

class TestCommandDispatcher(unittest.TestCase):
    def setUp(self):
        self.dispatcher = CommandDispatcher()

    @patch.object(CommandDispatcher, 'authenticate')
    def test_dispatch_unauthorized_user(self, mock_authenticate):
        mock_authenticate.return_value = False
        result = self.dispatcher.dispatch('command1', 'user3')
        self.assertEqual(result, 'Unauthorized user')

    @patch.object(CommandDispatcher, 'authenticate')
    def test_dispatch_invalid_command(self, mock_authenticate):
        mock_authenticate.return_value = True
        result = self.dispatcher.dispatch('invalid_command', 'user1')
        self.assertEqual(result, 'Invalid command')

    @patch.object(CommandDispatcher, 'authenticate')
    def test_dispatch_valid_command(self, mock_authenticate):
        mock_authenticate.return_value = True
        result = self.dispatcher.dispatch('command1', 'user1')
        self.assertEqual(result, 'Command1 executed')

if __name__ == '__main__':
    unittest.main()