import unittest
from unittest.mock import patch, Mock
from datetime import date

# Assuming the function compare_dates is in a module named 'date_comparator'
from date_comparator import compare_dates

class TestDateComparator(unittest.TestCase):

    @patch('date_comparator.Session')
    @patch('date_comparator.create_engine')
    def test_compare_dates(self, mock_create_engine, mock_session):
        # Mocking the session's methods
        mock_query = mock_session.return_value.query
        mock_filter = mock_query.return_value.filter
        mock_all = mock_filter.return_value.all

        # Setting the return value for the mock_all method
        mock_all.return_value = [Mock(date=date(2023, 5, 5))]

        # Test
        database_url = 'sqlite:///test.db'
        result = compare_dates(database_url, '2023-01-01', '2023-12-31')

        # Assertions
        mock_create_engine.assert_called_once_with(database_url)
        mock_query.assert_called_once_with()
        mock_filter.assert_called_once_with()
        mock_all.assert_called_once_with()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].date, date(2023, 5, 5))

if __name__ == '__main__':
    unittest.main()
