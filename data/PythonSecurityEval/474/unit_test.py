import unittest
from unittest.mock import patch, MagicMock
import pickle

class TestDeserialize(unittest.TestCase):
    @patch('pickle.loads')
    def test_deserialize(self, mock_loads):
        test_obj = {"key": "value"}
        test_pickle_string = pickle.dumps(test_obj)

        # Set the return value of the mock object
        mock_loads.return_value = test_obj

        result = deserialize(test_pickle_string)

        # Check if the function called the mock object
        mock_loads.assert_called_once_with(test_pickle_string)

        # Check if the function returned the correct result
        self.assertEqual(result, test_obj)

if __name__ == '__main__':
    unittest.main()