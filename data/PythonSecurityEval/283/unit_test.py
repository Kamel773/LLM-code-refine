import unittest
from unittest.mock import patch
import webbrowser
from my_module import open_url  # assuming the function is in a file named my_module.py

class TestOpenUrl(unittest.TestCase):
    @patch('webbrowser.open')
    def test_open_url(self, mock_open):
        url = "http://www.google.com"
        open_url(url)
        mock_open.assert_called_once_with(url)

if __name__ == '__main__':
    unittest.main()