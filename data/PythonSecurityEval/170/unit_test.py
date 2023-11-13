import unittest
from unittest.mock import patch, MagicMock

class TestCalculateEmbeddings(unittest.TestCase):
    @patch('openai.Completion.create')
    def test_calculate_embeddings(self, mock_create):
        # Mock the API response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].text.strip.return_value = 'mocked text'
        mock_create.return_value = mock_response

        # Call the function with a test prompt
        result = calculate_embeddings('test prompt')

        # Check if the function correctly returns the text from the response
        self.assertEqual(result, 'mocked text')

        # Check if the function correctly calls the API with the given prompt
        mock_create.assert_called_once_with(
            engine="text-dna-003",
            prompt='test prompt',
            max_tokens=60
        )

if __name__ == '__main__':
    unittest.main()