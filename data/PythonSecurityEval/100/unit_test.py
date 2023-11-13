import unittest
from unittest.mock import patch
from random import shuffle

class TestUniqueShuffler(unittest.TestCase):
    @patch('random.shuffle', side_effect=lambda x: x.reverse())
    def test_unique_shuffle(self, mock_shuffle):
        shuffler = UniqueShuffler()
        sequence = [1, 2, 3, 4, 5]
        first_result = shuffler.unique_shuffle(sequence)
        second_result = shuffler.unique_shuffle(sequence)
        self.assertNotEqual(first_result, second_result)

if __name__ == '__main__':
    unittest.main()