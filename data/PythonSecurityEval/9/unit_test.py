import unittest
from unittest.mock import patch, Mock
import os

class TestAppendDataFromURL(unittest.TestCase):

    @patch('requests.get')
    def test_append_data_from_url(self, mock_get):
        mock_resp_instance = Mock()
        mock_resp_instance.raise_for_status = Mock()
        mock_resp_instance.content = '<html><head><title>Test Page</title></head><body>This is a test</body></html>'.encode()
        mock_get.return_value = mock_resp_instance

        test_file = 'test.txt'
        append_data_from_url('http://test.com', test_file)

        with open(test_file, 'r') as f:
            contents = f.read()

        expected_contents = '<html>\n <head>\n  <title>\n   Test Page\n  </title>\n </head>\n <body>\n  This is a test\n </body>\n</html>\n'

        self.assertEqual(contents, expected_contents)

        if os.path.exists(test_file):
            os.remove(test_file)


if __name__ == '__main__':
    unittest.main()
