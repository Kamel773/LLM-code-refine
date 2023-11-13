import unittest
from unittest.mock import patch, Mock

class TestGetAssignments(unittest.TestCase):
    @patch('requests.get')
    def test_get_assignments(self, mock_get):
        mock_response = Mock()
        expected_result = [{"id": 1, "name": "Assignment 1"}, {"id": 2, "name": "Assignment 2"}]
        mock_response.json.return_value = expected_result
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        result = get_assignments(123, "your_access_token")

        self.assertEqual(result, expected_result)
        mock_get.assert_called_once_with(
            "https://canvas.instructure.com/api/v1/courses/123/assignments",
            headers={"Authorization": "Bearer your_access_token"}
        )

if __name__ == "__main__":
    unittest.main()