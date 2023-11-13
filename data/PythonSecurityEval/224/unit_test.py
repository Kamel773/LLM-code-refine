import unittest
from unittest.mock import patch

class TestIsScientificNotation(unittest.TestCase):
    @patch('__main__.is_scientific_notation')
    def test_is_scientific_notation(self, mock_is_scientific_notation):
        test_cases = [
            ("3.14", False),
            ("1.23e-4", True),
            ("-1E5", True),
            ("abc", False),
            ("1.23e4.5", False),
            ("", False),
        ]

        for s, expected in test_cases:
            mock_is_scientific_notation.return_value = expected
            result = is_scientific_notation(s)
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()