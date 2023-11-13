import unittest
from unittest import mock

class MyTestCase(unittest.TestCase):
    @mock.patch('my_module.requests.post')
    def test_send_dictionary_to_client(self, mock_post):
        # Set up the mock response
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        # Create a dictionary to send
        dictionary = {'key1': 'value1', 'key2': 'value2'}

        # Call the function
        status_code = send_dictionary_to_client(dictionary)

        # Assert that the mock HTTP request was called with the expected arguments
        mock_post.assert_called_once_with('http://example.com/api', json=json.dumps(dictionary))

        # Assert that the status code is correct
        self.assertEqual(status_code, 200)

if __name__ == '__main__':
    unittest.main()
