import unittest
from unittest.mock import patch
import logging
from your_module import log_user_action  # replace 'your_module' with the name of your module

class TestLogUserAction(unittest.TestCase):
    @patch('logging.info')
    def test_log_user_action(self, mock_info):
        user_id = '123'
        action = 'login'
        log_user_action(user_id, action)
        mock_info.assert_called_once_with(f'User {user_id} performed {action}')

if __name__ == '__main__':
    unittest.main()