import unittest
from unittest.mock import patch, mock_open
import my_module  # replace with the name of your module

class TestMyModule(unittest.TestCase):
    @patch('my_module.requests.get')
    @patch('my_module.csv.writer')
    def test_main(self, mock_writer, mock_get):
        mock_response = mock_get.return_value
        mock_response.text = '<div class="quote"><span class="text">Quote text</span><small class="author">Author name</small></div>'
        mock_file = mock_open()
        with patch('my_module.open', mock_file):
            my_module.main()
        mock_get.assert_called_once_with('http://quotes.toscrape.com/')
        mock_writer.return_value.writerows.assert_called_once()

if __name__ == "__main__":
    unittest.main()