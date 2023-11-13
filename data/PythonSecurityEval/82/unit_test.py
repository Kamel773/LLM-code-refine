import unittest
from unittest.mock import patch, Mock
import pandas as pd

class TestInsertDataFrameToDB(unittest.TestCase):

    def setUp(self):
        self.sample_data = {
            'col1': [1, 2, 3],
            'col2': ['A', 'B', 'C']
        }
        self.df = pd.DataFrame(self.sample_data)
        self.database_url = "sqlite:///test.db"
        self.table_name = "test_table"

    @patch('sqlalchemy.create_engine')
    def test_insert_dataframe_to_db(self, mock_create_engine):
        mock_engine = Mock()
        mock_create_engine.return_value = mock_engine

        insert_dataframe_to_db(self.df, self.database_url, self.table_name)

        mock_create_engine.assert_called_once_with(self.database_url)
        mock_engine.connect.assert_called_once()

if __name__ == '__main__':
    unittest.main()
