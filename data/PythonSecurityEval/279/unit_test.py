import unittest
from unittest.mock import patch, mock_open
import base64

class TestDecodeBase64ToImage(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    @patch("PIL.Image.Image.save")
    def test_decode_base64_to_image(self, mock_save, mock_open):
        base64_string = base64.b64encode(b"test data").decode()
        output_path = "/path/to/output/image.jpg"

        result = decode_base64_to_image(base64_string, output_path)

        self.assertTrue(result)
        mock_save.assert_called_once_with(output_path)

if __name__ == "__main__":
    unittest.main()