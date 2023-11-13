import unittest
from unittest.mock import patch, MagicMock
import pickle

class TestDeserializeObject(unittest.TestCase):
    @patch('pickle.loads')
    def test_deserialize_object(self, mock_loads):
        mock_loads.return_value = 'deserialized object'
        serialized_object = MagicMock()

        result = deserialize_object(serialized_object)

        mock_loads.assert_called_once_with(serialized_object)
        self.assertEqual(result, 'deserialized object')

if __name__ == '__main__':
    unittest.main()