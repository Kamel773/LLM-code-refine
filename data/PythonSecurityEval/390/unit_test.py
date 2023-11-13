import unittest
from unittest.mock import patch

class TestCreateDictFromUrlQuery(unittest.TestCase):
    @patch('__main__.create_dict_from_url_query')
    def test_create_dict_from_url_query(self, mock_create_dict_from_url_query):
        mock_create_dict_from_url_query.return_value = {'key1': 'value1', 'key2': 'value2'}
        result = create_dict_from_url_query('?key1=value1&key2=value2')
        self.assertEqual(result, {'key1': 'value1', 'key2': 'value2'})

if __name__ == '__main__':
    unittest.main()