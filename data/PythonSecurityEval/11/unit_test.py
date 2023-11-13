import unittest
from unittest.mock import mock_open, patch
import pickle

class TestSerializeObject(unittest.TestCase):
    @patch('pickle.dump')
    @patch('builtins.open', new_callable=mock_open)
    def test_serialize_object(self, mock_open, mock_pickle):
        test_object = {"key": "value"}
        serialize_object(test_object, 'testfile')

        # Check if the file was opened in write binary mode
        mock_open.assert_called_once_with('testfile', 'wb')

        # Check if the object was serialized using pickle
        mock_pickle.assert_called_once_with(test_object, mock_open())

if __name__ == '__main__':
    unittest.main()