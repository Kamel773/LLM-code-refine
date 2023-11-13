import unittest
from unittest.mock import patch, mock_open
import pandas as pd

class TestJsonToDataframe(unittest.TestCase):
    @patch('pandas.read_json', return_value=pd.DataFrame({'A': [1, 2, 3]}))
    def test_json_to_dataframe(self, mock_read_json):
        mock_file_path = "mock_file_path.json"
        expected_df = pd.DataFrame({'A': [1, 2, 3]})
        result_df = json_to_dataframe(mock_file_path)
        mock_read_json.assert_called_once_with(mock_file_path)
        pd.testing.assert_frame_equal(result_df, expected_df)

if __name__ == '__main__':
    unittest.main()