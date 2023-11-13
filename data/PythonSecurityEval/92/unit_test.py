import unittest

class TestConllToSpacy(unittest.TestCase):

    def test_conversion(self):
        conll_example = """Hello O
World O
, O
my O
name O
is O
Alice B-PER
. O

This O
is O
Bob B-PER
. O"""

        expected_output = [
            ('Hello World , my name is Alice .', {'entities': [(24, 29, 'PER')]}),
            ('This is Bob .', {'entities': [(8, 11, 'PER')]})
        ]

        result = conll_to_spacy(conll_example)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
