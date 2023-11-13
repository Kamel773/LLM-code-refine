import unittest
from unittest.mock import patch, Mock

class TestExtractTextFromImage(unittest.TestCase):
    @patch('pytesseract.image_to_string', return_value='mocked text')
    @patch('PIL.Image.open')
    def test_extract_text_from_image(self, mock_open, mock_image_to_string):
        mock_open.return_value = Mock()
        result = extract_text_from_image('mock_path')
        self.assertEqual(result, 'mocked text')
        mock_open.assert_called_once_with('mock_path')
        mock_image_to_string.assert_called_once_with(mock_open.return_value)

if __name__ == '__main__':
    unittest.main()