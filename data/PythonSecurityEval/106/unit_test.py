import unittest

class TestExtractTablesAndColumns(unittest.TestCase):
    def test_extract_tables_and_columns(self):
        query = "SELECT column1, column2 FROM table1 JOIN table2 ON table1.id = table2.id"
        tables, columns = extract_tables_and_columns(query)
        self.assertEqual(tables, ['table1', 'table2'])
        self.assertEqual(columns, ['column1', 'column2'])

if __name__ == '__main__':
    unittest.main()