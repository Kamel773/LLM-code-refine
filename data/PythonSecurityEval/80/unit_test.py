import unittest
from unittest.mock import patch, Mock
import pandas as pd

class TestImportSQLTables(unittest.TestCase):

    @patch('pandas.read_sql_table')
    @patch('sqlalchemy.create_engine')
    def test_import_sql_tables(self, mock_create_engine, mock_read_sql_table):
        # Mock data
        mock_df1 = pd.DataFrame({'a': [1, 2, 3]})
        mock_df2 = pd.DataFrame({'b': [4, 5, 6]})
        
        # Mock return values
        mock_read_sql_table.side_effect = [mock_df1, mock_df2]
        
        # Test function
        engine_url = "sqlite:///test.db"
        tables = import_sql_tables(engine_url, ["table1", "table2"])
        
        # Assertions
        self.assertIn("table1", tables)
        self.assertIn("table2", tables)
        self.assertTrue(tables["table1"].equals(mock_df1))
        self.assertTrue(tables["table2"].equals(mock_df2))
        mock_create_engine.assert_called_once_with(engine_url)
        mock_read_sql_table.assert_any_call("table1", mock_create_engine.return_value)
        mock_read_sql_table.assert_any_call("table2", mock_create_engine.return_value)

if __name__ == "__main__":
    unittest.main()
