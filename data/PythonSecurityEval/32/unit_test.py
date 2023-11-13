import unittest
import unittest.mock as mock
from unittest.mock import mock_open
import pickle

class TestListIo(unittest.TestCase):
    
    @mock.patch("builtins.open", new_callable=mock_open)
    @mock.patch("pickle.dump")
    def test_dump_list_to_pickle(self, mock_pickle_dump, mock_open):
        file_path = "test_file.pkl"
        data = [1, 2, 3]
        
        dump_list_to_pickle(file_path, data)
        
        # test if the functions were called with the right parameters
        mock_open.assert_called_with(file_path, 'wb')
        mock_pickle_dump.assert_called_with(data, mock_open.return_value.__enter__.return_value)
        
    @mock.patch("builtins.open", new_callable=mock_open)
    @mock.patch("pickle.load")
    def test_load_list_from_pickle(self, mock_pickle_load, mock_open):
        file_path = "test_file.pkl"
        data = [1, 2, 3]
        
        mock_pickle_load.return_value = data  # mock return value for pickle.load

        result = load_list_from_pickle(file_path)
        
        # test if the functions were called with the right parameters
        mock_open.assert_called_with(file_path, 'rb')
        mock_pickle_load.assert_called_with(mock_open.return_value.__enter__.return_value)

        # check if the function returns the correct result
        self.assertEqual(result, data)

if __name__ == '__main__':
    unittest.main()
