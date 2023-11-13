import unittest
from unittest.mock import patch, MagicMock
import qrcode.main

class TestGenerateQR(unittest.TestCase):
    @patch('qrcode.main.QRCode')
    def test_generate_qr(self, mock_qr):
        mock_qr.return_value.make_image.return_value.save = MagicMock()
        data = 'Test string'
        generate_qr(data)
        mock_qr.assert_called_once_with(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        mock_qr.return_value.add_data.assert_called_once_with(data)
        mock_qr.return_value.make.assert_called_once_with(fit=True)
        mock_qr.return_value.make_image.assert_called_once_with(fill_color="black", back_color="white")
        mock_qr.return_value.make_image.return_value.save.assert_called_once_with('qrcode.png')

if __name__ == '__main__':
    unittest.main()