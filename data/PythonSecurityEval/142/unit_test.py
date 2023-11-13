import unittest
from unittest.mock import patch
from io import StringIO

class TestEvaluateExpression(unittest.TestCase):
    def test_evaluate_expression(self):
        with patch('builtins.input', return_value='2 + 2'):
            self.assertEqual(evaluate_expression(input()), 4)

        with patch('builtins.input', return_value='5 * 5'):
            self.assertEqual(evaluate_expression(input()), 25)

        with patch('builtins.input', return_value='invalid expression'):
            self.assertEqual(evaluate_expression(input()), "name 'invalid' is not defined")

if __name__ == '__main__':
    unittest.main()