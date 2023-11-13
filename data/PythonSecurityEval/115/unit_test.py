import unittest
from unittest.mock import Mock, patch
from xml.etree.ElementTree import Element, ElementTree

class TestCountElements(unittest.TestCase):
    @patch('xml.etree.ElementTree.ElementTree.findall')
    def test_count_elements(self, mock_findall):
        mock_tree = Mock(spec=ElementTree)
        mock_findall.return_value = [Mock(spec=Element) for _ in range(5)]
        self.assertEqual(count_elements(mock_tree), 5)
        mock_findall.assert_called_once_with('.//*')

if __name__ == '__main__':
    unittest.main()