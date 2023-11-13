from unittest.mock import patch, Mock

class TestDecodeMarshalledData(unittest.TestCase):
    @patch('marshal.loads')
    def test_decode_marshalled_data(self, mock_loads):
        # Set the mock's return value and side effect
        mock_loads.return_value = 1
        mock_loads.side_effect = [1, ValueError("bad marshal data")]

        # Test valid input
        self.assertEqual(decode_marshalled_data(b'\x03\x00\x00\x00\x00\x00\x00\x00\x00\x01'), 1)
        mock_loads.assert_called_once_with(b'\x03\x00\x00\x00\x00\x00\x00\x00\x00\x01')

        # Test invalid input
        mock_loads.reset_mock()
        self.assertIsNone(decode_marshalled_data("not a valid marshalled string"))
        mock_loads.assert_called_once_with("not a valid marshalled string")


if __name__ == '__main__':
    unittest.main()
