import unittest
from unittest.mock import patch
from flask import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('os.system')
    def test_execute_command(self, mock_os_system):
        mock_os_system.return_value = 0
        response = self.app.post('/execute', data=json.dumps({'command': 'echo hello'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'result': 0})
        mock_os_system.assert_called_once_with('echo hello')

if __name__ == '__main__':
    unittest.main()