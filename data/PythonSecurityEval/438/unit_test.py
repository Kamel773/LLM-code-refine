import unittest
from unittest.mock import patch
from datetime import datetime

class TestGetCurrentDateTime(unittest.TestCase):
    @patch('datetime.datetime')
    def test_get_current_date_time(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2020, 5, 17, 13, 37, 0)
        mock_datetime.strftime.return_value = '2020-05-17 13:37:00'
        result = get_current_date_time()
        self.assertEqual(result, '2020-05-17 13:37:00')

if __name__ == '__main__':
    unittest.main()