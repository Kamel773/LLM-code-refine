from unittest.mock import patch, Mock
import pandas as pd

class TestConvertNumbersToMd5(unittest.TestCase):
    @patch('hashlib.md5')
    def test_convert_numbers_to_md5(self, mock_md5):
        mock_md5.return_value.hexdigest.return_value = 'md5_hash'

        test_df = pd.DataFrame({
            'number': [1, 2, 3, 4, 5]
        })
        result_df = convert_numbers_to_md5(test_df, 'number')

        # assert that hashlib.md5 was called the correct number of times
        self.assertEqual(mock_md5.call_count, len(test_df))

        # assert that the result is as expected
        expected_df = pd.DataFrame({
            'number': ['md5_hash'] * len(test_df)
        })
        pd.testing.assert_frame_equal(result_df, expected_df)

if __name__ == '__main__':
    unittest.main()
