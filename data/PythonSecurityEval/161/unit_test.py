import unittest
from unittest.mock import patch, call

class TestKillProcess(unittest.TestCase):
    @patch('os.kill')
    def test_kill_process(self, mock_kill):
        pid = 1234
        kill_process(pid)
        mock_kill.assert_called_once_with(pid, signal.SIGTERM)

if __name__ == '__main__':
    unittest.main()