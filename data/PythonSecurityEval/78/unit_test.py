import unittest
from unittest.mock import Mock, patch
from sqlalchemy.orm import sessionmaker

class TestSelectNullValues(unittest.TestCase):

    @patch('your_module_name.select_null_values')
    def test_select_null_values(self, mock_select_null_values):
        # Mock the session and column
        mock_session = Mock()
        mock_column = Mock()

        # Call the function
        select_null_values(mock_session, mock_column)

        # Assert that the filter method was called with the correct arguments
        mock_session.query.assert_called_with(Sample)
        mock_session.query().filter.assert_called_with(mock_column == None)

if __name__ == '__main__':
    unittest.main()