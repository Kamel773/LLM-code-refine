import unittest
from unittest.mock import patch, MagicMock
from my_module import get_user_info  # assuming the function is in a file named my_module.py

class TestGetUserInfo(unittest.TestCase):
    @patch('my_module.boto3.resource')
    def test_get_user_info(self, mock_resource):
        # Mock the DynamoDB Table resource
        mock_table = MagicMock()
        mock_resource.return_value.Table.return_value = mock_table

        # Mock the response from DynamoDB
        mock_response = {
            'Item': {
                'username': 'test_user',
                'password': 'test_password',
                'email': 'test_user@example.com'
            }
        }
        mock_table.get_item.return_value = mock_response

        # Call the function with the test data
        result = get_user_info('test_user', 'test_password')

        # Assert that the function made the calls as expected
        mock_resource.assert_called_once_with('dynamodb')
        mock_resource.return_value.Table.assert_called_once_with('Users')
        mock_table.get_item.assert_called_once_with(Key={'username': 'test_user', 'password': 'test_password'})

        # Assert that the function returned the expected result
        self.assertEqual(result, mock_response['Item'])

if __name__ == '__main__':
    unittest.main()