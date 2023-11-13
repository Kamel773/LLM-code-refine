from unittest.mock import mock_open, patch
import io

class TestGetRootHandle(unittest.TestCase):

    def test_get_root_handle(self):
        mock_xml_data = """<?xml version="1.0"?>
                            <root>
                                <element1>Text1</element1>
                                <element2>Text2</element2>
                            </root>
                        """
        m = mock_open(read_data=mock_xml_data)
        with patch('builtins.open', m):
            root_handle = get_root_handle(io.StringIO(mock_xml_data))
            self.assertEqual(root_handle.tag, "root")


if __name__ == "__main__":
    unittest.main()
