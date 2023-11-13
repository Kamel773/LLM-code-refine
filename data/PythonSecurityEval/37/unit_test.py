import unittest
from unittest.mock import patch, Mock

class TestLoadSerializedObject(unittest.TestCase):
    @patch('requests.get')
    def test_load_serialized_object(self, mock_get):
        mock_response = Mock()
        mock_response.content = pickle.dumps("test object")
        mock_get.return_value = mock_response

        result = load_serialized_object("http://dummyurl.com")
        self.assertEqual(result, "test object")

if __name__ == '__main__':
    unittest.main()
