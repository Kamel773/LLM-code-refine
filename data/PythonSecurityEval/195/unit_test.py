import unittest
from unittest.mock import patch

class TestProcessData(unittest.TestCase):
    @patch('__main__.foo')
    def test_process_data(self, mock_foo):
        mock_foo.side_effect = [{"basename": "file2", "data": "data2"}, 
                                {"basename": "file1", "data": "data1"}, 
                                {"basename": "file3", "data": "data3"}]
        expected_result = [{'basename': 'file1', 'data': 'data1'}, 
                           {'basename': 'file2', 'data': 'data2'}, 
                           {'basename': 'file3', 'data': 'data3'}]
        self.assertEqual(process_data(), expected_result)

if __name__ == '__main__':
    unittest.main()