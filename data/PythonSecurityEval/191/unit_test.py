import unittest
from unittest.mock import patch, Mock

class TestIncrementSharedVar(unittest.TestCase):
    @patch('threading.Lock')
    @patch('time.sleep')  # we patch sleep to make the test run faster
    def test_increment_shared_var(self, mock_sleep, mock_lock):
        global shared_var
        shared_var = 0

        mock_lock_instance = Mock()
        mock_lock.return_value = mock_lock_instance

        increment_shared_var()

        # Check if lock was used correctly
        mock_lock.assert_called_once()
        mock_lock_instance.__enter__.assert_called_once()
        mock_lock_instance.__exit__.assert_called_once()

        # Check if sleep was called
        mock_sleep.assert_called_once_with(0.1)

        # Check if shared_var was incremented
        self.assertEqual(shared_var, 1)

if __name__ == '__main__':
    unittest.main()