import sqlite3
import pickle
import unittest
from unittest.mock import patch, call
from typing import Any

# unit test
class TestPickleAndStore(unittest.TestCase):

    @patch('sqlite3.connect')
    @patch('pickle.dumps')
    def test_pickle_and_store(self, mock_pickle, mock_connect):
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value
        dictionary = {"name": "John", "age": 30}

        pickle_and_store(dictionary, mock_conn)
        
        mock_pickle.assert_called_once_with(dictionary)
        mock_connect.assert_called_once_with(':memory:')
        mock_cursor.execute.assert_called_once_with("INSERT INTO dictionary(data) VALUES (?)", 
                                                    (sqlite3.Binary(mock_pickle.return_value),))
        mock_conn.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
