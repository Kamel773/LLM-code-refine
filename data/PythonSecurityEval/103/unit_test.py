import unittest
from unittest.mock import patch, Mock
import decimal

class TestConvertDecimalToSQLiteNumeric(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_convert_decimal_to_sqlite_numeric(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = ['123.45']

        result = convert_decimal_to_sqlite_numeric(decimal.Decimal('123.45'))

        self.assertEqual(result, '123.45')
        mock_connect.assert_called_once_with(":memory:")
        mock_cursor.execute.assert_any_call("create table test (num numeric)")
        mock_cursor.execute.assert_any_call("insert into test (num) values (?)", (decimal.Decimal('123.45'),))
        mock_cursor.execute.assert_any_call("select * from test")
        mock_connect.return_value.commit.assert_called_once()
        mock_connect.return_value.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()