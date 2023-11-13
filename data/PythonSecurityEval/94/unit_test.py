import unittest
from unittest.mock import patch, mock_open
from io import StringIO

class TestMergeFieldsInCSV(unittest.TestCase):

    def test_merge_fields(self):
        csv_data = "Name,Age,Location\nJohn,25,USA\nDoe,30,Canada"
        expected_output = "Name Age,Location\nJohn 25 USA,\nDoe 30 Canada,\n"
        
        result = merge_fields_in_csv(csv_data, 0, 1)
        self.assertEqual(result, expected_output)

    @patch('builtins.open', new_callable=mock_open, read_data="Name,Age,Location\nJohn,25,USA\nDoe,30,Canada")
    def test_merge_fields_with_mock_file(self, mock_file):
        with open('dummy.csv', 'r') as f:
            csv_data = f.read()

        expected_output = "Name Age,Location\nJohn 25 USA,\nDoe 30 Canada,\n"
        
        result = merge_fields_in_csv(csv_data, 0, 1)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
