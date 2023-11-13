import unittest
import io
from unittest.mock import patch

class TestLoopThroughXml(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_loop_through_xml(self, mock_stdout):
        mock_xml = """<?xml version="1.0"?>
        <root>
            <element1>Text1</element1>
            <element2>Text2</element2>
        </root>
        """
        loop_through_xml(io.StringIO(mock_xml))
        expected_output = "Tag: root, Text: \n    \n    \nTag: element1, Text: Text1\nTag: element2, Text: Text2\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()