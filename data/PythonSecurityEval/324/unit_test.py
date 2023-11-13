import unittest
from unittest.mock import patch, Mock
import pandas as pd

class TestReadExcelToDf(unittest.TestCase):
    @patch('pandas.read_excel')
    def test_read_excel_to_df(self, mock_read_excel):
        mock_df = Mock(spec=pd.DataFrame)
        mock_read_excel.return_value = mock_df

        result = read_excel_to_df('mock_file_path')

        mock_read_excel.assert_called_once_with('mock_file_path')
        self.assertEqual(result, mock_df)

if __name__ == '__main__':
    unittest.main()