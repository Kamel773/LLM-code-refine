import unittest
from unittest.mock import patch, Mock
import pandas as pd

class TestCSVFunctions(unittest.TestCase):
    @patch('pandas.read_csv')
    def test_read_csv_file(self, mock_read_csv):
        mock_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        mock_read_csv.return_value = mock_df

        result = read_csv_file('dummy_path')
        mock_read_csv.assert_called_once_with('dummy_path')
        pd.testing.assert_frame_equal(result, mock_df)

    @patch('pandas.DataFrame.to_csv')
    def test_write_csv_file(self, mock_to_csv):
        mock_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        result = write_csv_file(mock_df, 'dummy_path')
        mock_to_csv.assert_called_once_with('dummy_path', index=False)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()