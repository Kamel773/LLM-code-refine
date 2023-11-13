import unittest
from unittest.mock import patch

class TestFetchData(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_data(self, mock_get):
        # Here, we set the response from the mocked get request
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'mocked data'

        url = 'http://mocked_url.com'
        data = fetch_data(url)
        self.assertEqual(data, 'mocked data')
        mock_get.assert_called_once_with(url)

if __name__ == "__main__":
    unittest.main()
