import unittest
from unittest.mock import patch
from datetime import datetime

class TestGetCurrentDateTime(unittest.TestCase):
    @patch('datetime.datetime')
    def test_get_current_date_time(self, mock_datetime):
        mock_datetime.now.return_value.strftime.return_value = '2022-01-01 00:00:00'
        result = get_current_date_time()
        self.assertEqual(result, '2022-01-01 00:00:00')

if __name__ == '__main__':
    unittest.main()