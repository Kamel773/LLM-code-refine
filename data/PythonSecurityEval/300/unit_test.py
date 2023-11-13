import unittest
from unittest.mock import patch, mock_open
import pandas as pd

class TestCsvToDataframe(unittest.TestCase):
    @patch('pandas.read_csv')
    def test_csv_to_dataframe(self, mock_read_csv):
        mock_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        mock_read_csv.return_value = mock_data

        result = csv_to_dataframe('dummy_path')

        mock_read_csv.assert_called_once_with('dummy_path')
        pd.testing.assert_frame_equal(result, mock_data)

if __name__ == '__main__':
    unittest.main()