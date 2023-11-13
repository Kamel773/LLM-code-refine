import unittest
from unittest.mock import patch, Mock
from your_module import list_tables  # Assuming the function is in 'your_module.py'

class TestListTables(unittest.TestCase):

    @patch('your_module.create_engine')
    @patch('your_module.MetaData')
    def test_list_tables(self, MockMetaData, MockCreateEngine):
        # Mock the engine and metadata
        mock_engine = Mock()
        mock_meta = Mock()
        mock_table_1 = Mock()
        mock_table_2 = Mock()
        
        mock_table_1.name = "table1"
        mock_table_2.name = "table2"
        
        mock_meta.sorted_tables = [mock_table_1, mock_table_2]
        MockMetaData.return_value = mock_meta
        MockCreateEngine.return_value = mock_engine

        # Call the function
        result = list_tables("mock://database.url")

        # Assert the expected result
        self.assertEqual(result, ["table1", "table2"])

if __name__ == "__main__":
    unittest.main()
