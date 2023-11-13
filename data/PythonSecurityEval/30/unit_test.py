import unittest
from unittest import mock
from unittest.mock import mock_open
import pickle

class TestPickleLoad(unittest.TestCase):

    @mock.patch('pickle.load')
    @mock.patch('builtins.open', new_callable=mock_open)
    def test_load_pickle_file(self, mock_open, mock_pickle_load):
        mock_pickle_load.return_value = {'key': 'value'}
        result = load_pickle_file('test_file_path.pkl')

        # Assert open was called with the correct file path and mode
        mock_open.assert_called_once_with('test_file_path.pkl', 'rb')
        self.assertEqual(result, {'key': 'value'})

    @mock.patch('pickle.load')
    @mock.patch('builtins.open', new_callable=mock_open)
    def test_load_pickle_file_error(self, mock_open, mock_pickle_load):
        mock_open.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            load_pickle_file('non_existent_file.pkl')


if __name__ == "__main__":
    unittest.main()
