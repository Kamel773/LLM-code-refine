import unittest
from unittest.mock import Mock, patch

class TestReadTruncatedData(unittest.TestCase):
    @patch('select.select')
    @patch.object(telnetlib.Telnet, 'read_eager')
    def test_read_truncated_data(self, mock_read_eager, mock_select):
        # Arrange
        mock_read_eager.side_effect = [b'data', b'', b'data', b'']
        mock_select.side_effect = [[1], [], [1], []]

        telnet = telnetlib.Telnet()
        timeout = 0.5

        # Act
        data = read_truncated_data(telnet, timeout)

        # Assert
        self.assertEqual(data, b'datadata')
        mock_select.assert_called_with([telnet], [], [], timeout)
        mock_read_eager.assert_called()

if __name__ == '__main__':
    unittest.main()
