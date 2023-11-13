import unittest
from unittest.mock import patch, MagicMock
import extract_metadata

class TestExtractMetadata(unittest.TestCase):
    @patch('PyPDF2.PdfFileReader')
    def test_extract_metadata(self, mock_reader):
        mock_pdf = MagicMock()
        mock_reader.return_value = mock_pdf
        mock_pdf.getDocumentInfo.return_value = {
            '/Title': 'Test PDF',
            '/Author': 'Test Author',
            '/Subject': 'Test Subject',
            '/Producer': 'Test Producer',
            '/CreationDate': 'D:20220101000000'
        }

        result = extract_metadata.extract_metadata('test.pdf')

        self.assertEqual(result['/Title'], 'Test PDF')
        self.assertEqual(result['/Author'], 'Test Author')
        self.assertEqual(result['/Subject'], 'Test Subject')
        self.assertEqual(result['/Producer'], 'Test Producer')
        self.assertEqual(result['/CreationDate'], 'D:20220101000000')

if __name__ == '__main__':
    unittest.main()