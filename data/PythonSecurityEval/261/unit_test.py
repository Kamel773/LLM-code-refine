import unittest
from unittest.mock import patch, mock_open
import PyPDF2
from your_module import extract_metadata  # replace 'your_module' with the name of your module

class TestExtractMetadata(unittest.TestCase):
    @patch('PyPDF2.PdfFileReader')
    @patch('builtins.open', new_callable=mock_open, read_data=b"PDF data")
    def test_extract_metadata(self, mock_file, mock_reader):
        mock_metadata = {
            '/Title': 'Test PDF',
            '/Author': 'Test Author',
            '/Subject': 'Test Subject',
            '/Producer': 'Test Producer',
            '/CreationDate': 'D:20220101000000'
        }
        mock_reader.return_value.getDocumentInfo.return_value = mock_metadata

        result = extract_metadata('test.pdf')

        mock_file.assert_called_once_with('test.pdf', 'rb')
        mock_reader.assert_called_once_with(mock_file.return_value)
        self.assertEqual(result, mock_metadata)

if __name__ == '__main__':
    unittest.main()