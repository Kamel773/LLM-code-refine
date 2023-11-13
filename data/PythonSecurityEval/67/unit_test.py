from unittest.mock import mock_open, patch

class TestLoadProcessData(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data=marshal.dumps({"key1": "value1", "key2": "value2"}))
    def test_load_process_data(self, mock_file):
        file_path = "fake_path"
        result = load_process_data(file_path)
        mock_file.assert_called_once_with(file_path, 'rb')
        self.assertEqual(result, 2)  # We have 2 keys in the mock dictionary

if __name__ == '__main__':
    unittest.main()
