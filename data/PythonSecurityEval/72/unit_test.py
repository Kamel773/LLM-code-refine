import unittest
from unittest.mock import patch

class TestExtractDBAndTable(unittest.TestCase):
    @patch('__main__.extract_db_and_table')
    def test_extract_db_and_table(self, mock_extract):
        # Mock the return value of the function
        mock_extract.return_value = ('test_db', 'test_table')

        # Call the function with a sample query
        db_name, table_name = extract_db_and_table('use db test_db test_table')

        # Assert that the function returned the correct values
        self.assertEqual(db_name, 'test_db')
        self.assertEqual(table_name, 'test_table')

if __name__ == '__main__':
    unittest.main()