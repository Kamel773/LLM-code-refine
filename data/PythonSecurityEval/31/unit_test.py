import unittest
from unittest import mock
from unittest.mock import mock_open

class TestReadPickle(unittest.TestCase):

    @mock.patch('pickle.load')
    @mock.patch('builtins.open', new_callable=mock_open)
    def test_read_pickle_file(self, mock_open, mock_pickle_load):
        mock_pickle_load.return_value = "mock data"
        result = read_pickle_file('path/to/mockfile')

        # Assert the file was opened
        mock_open.assert_called_once_with('path/to/mockfile', 'rb')

        # Assert pickle.load was called with the opened file
        mock_pickle_load.assert_called_once()

        # Assert the function returns the mock data
        self.assertEqual(result, "mock data")

if __name__ == "__main__":
    unittest.main()
