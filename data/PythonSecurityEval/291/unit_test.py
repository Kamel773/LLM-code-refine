import unittest
from unittest.mock import patch

class TestValidateSession(unittest.TestCase):
    @patch('active_sessions', ['123', '456', '789'])
    def test_validate_session(self):
        self.assertTrue(validate_session('123', active_sessions))
        self.assertFalse(validate_session('000', active_sessions))

if __name__ == '__main__':
    unittest.main()