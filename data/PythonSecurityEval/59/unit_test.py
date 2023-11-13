import unittest
from unittest.mock import mock_open, patch
import your_module  # replace with the name of the module where you defined the function

class TestStoreCreditCardInfo(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_store_credit_card_info(self, mock_open):
        your_module.store_credit_card_info('John Doe', '1234567812345678', '12/24', '123')
        mock_open.assert_called_once_with('credit_card_info.txt', 'a')
        mock_open().write.assert_called_once_with('Name: John Doe, Card Number: 1234567812345678, Expiry Date: 12/24, CVV: 123\n')

if __name__ == '__main__':
    unittest.main()