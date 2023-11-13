import unittest
from unittest.mock import patch, Mock
from your_module_name import query_to_json  # Replace 'your_module_name' with the actual module name

class TestQueryToJson(unittest.TestCase):

    def test_query_to_json(self):
        # Sample MongoDB query
        query = {
            "name": "John",
            "age": {"$gte": 25}
        }

        # Expected JSON string
        expected_json = '{"name": "John", "age": {"$gte": 25}}'

        # Call the function
        result = query_to_json(query)

        # Assert that the result matches the expected JSON string
        self.assertEqual(result, expected_json)

if __name__ == "__main__":
    unittest.main()
