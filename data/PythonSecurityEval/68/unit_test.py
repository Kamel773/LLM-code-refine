from unittest.mock import mock_open, patch

class TestChecksum(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data=b'dummy file data')
    def test_compute_checksum(self, mock_file):
        mock_file_path = '/path/to/dummy/file'

        # Known md5 checksum for 'dummy file data'
        expected_checksum = '5c6ffbdd40d9556b73a21e63c3e0e904'

        result_checksums = compute_checksum([mock_file_path])
        
        self.assertEqual(len(result_checksums), 1)
        self.assertEqual(result_checksums[0], expected_checksum)


if __name__ == '__main__':
    unittest.main()
