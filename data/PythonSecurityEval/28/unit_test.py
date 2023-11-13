class TestFormatDateWithMako(unittest.TestCase):
    def test_format_date(self):
        # Create a date object for testing
        date = datetime.date(2023, 6, 23)
        
        # Define the expected formatted date
        expected_date = '2023-06-23'

        # Mock the Mako template rendering
        with mock.patch.object(Template, 'render') as mock_render:
            # Configure the mock to return the date argument
            mock_render.return_value = expected_date

            # Call the function under test
            formatted_date = format_date_with_mako(date)

            # Assert that the Mako template render was called with the expected arguments
            mock_render.assert_called_once_with(date_obj=date)

        # Assert the result matches the expected output
        self.assertEqual(formatted_date, expected_date)

if __name__ == '__main__':
    unittest.main()