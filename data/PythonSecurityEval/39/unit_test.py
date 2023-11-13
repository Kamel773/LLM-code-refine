import unittest
from unittest.mock import patch
import random

class TestUniqueRandomChoice(unittest.TestCase):

    @patch('random.shuffle')
    def test_unique_random_choice(self, mock_shuffle):
        # Arrange
        items = [1, 2, 3, 4, 5]
        expected_items = list(items)  # Create a copy of the items
        mock_shuffle.side_effect = lambda x: x.reverse()  # Just reverse the list on shuffle

        # Act
        actual_items = list(unique_random_choice(items))  # Consume all items from the generator

        # Assert
        self.assertListEqual(expected_items, actual_items)
        self.assertEqual(len(set(actual_items)), len(expected_items))  # All items are unique

if __name__ == '__main__':
    unittest.main()
