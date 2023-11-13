import unittest
from unittest import mock
from pandas.util.testing import assert_frame_equal
import pandas as pd

class TestCsvToDataframe(unittest.TestCase):
    @mock.patch('pandas.read_csv')
    def test_csv_to_dataframe(self, mock_read_csv):
        mock_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        mock_read_csv.return_value = mock_df

        result = csv_to_dataframe('dummy_path')
        assert_frame_equal(result, mock_df)

        mock_read_csv.assert_called_once_with('dummy_path')

if __name__ == '__main__':
    unittest.main()