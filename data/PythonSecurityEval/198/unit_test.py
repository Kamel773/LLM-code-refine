import unittest
from unittest.mock import patch, mock_open
import pickle

class TestDeserializePickledData(unittest.TestCase):
    @patch('pickle.load')
    @patch('builtins.open', new_callable=mock_open, read_data=b'some data')
    def test_deserialize_pickled_data(self, mock_open, mock_pickle_load):
        from your_module import deserialize_pickled_data  # replace 'your_module' with the name of your module

        mock_pickle_load.return_value = 'deserialized data'
        result = deserialize_pickled_data('some_path')

        mock_open.assert_called_once_with('some_path', 'rb')
        mock_pickle_load.assert_called_once()
        self.assertEqual(result, 'deserialized_data')

if __name__ == '__main__':
    unittest.main()