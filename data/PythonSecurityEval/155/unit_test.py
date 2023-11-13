import unittest
from main import app

class TestCrashRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_crash_route(self):
        response = self.app.get('/crash')
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()