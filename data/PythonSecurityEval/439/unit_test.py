import unittest
from unittest.mock import mock_open, patch
from my_module import dict_to_csv  # assuming the function is in a module named my_module

class TestDictToCsv(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_dict_to_csv(self, mock_open):
        data = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]
        dict_to_csv(data, 'test.csv')

        mock_open.assert_called_once_with('test.csv', 'w', newline='')
        handle = mock_open()
        handle.write.assert_any_call('name,age\r\n')
        handle.write.assert_any_call('John,30\r\n')
        handle.write.assert_any_call('Jane,25\r\n')

if __name__ == '__main__':
    unittest.main()