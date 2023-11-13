import unittest
from unittest.mock import patch, mock_open
import my_module  # replace this with the name of the module where you have the above function

class TestMyModule(unittest.TestCase):

    @patch('zipfile.ZipFile')
    def test_extract_zip_file(self, mock_zip):
        mock_zip.return_value.__enter__.return_value.extractall.return_value = True
        result = my_module.extract_zip_file('test.zip', '/tmp/')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()