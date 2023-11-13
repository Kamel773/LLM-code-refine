import unittest
from unittest.mock import MagicMock, patch
from sqlalchemy.exc import NoSuchTableError

class TestDeleteTable(unittest.TestCase):

    @patch('sqlalchemy.MetaData')
    def test_delete_existing_table(self, MockedMetaData):
        # Setup
        mock_engine = MagicMock()
        mock_table = MagicMock()
        MockedMetaData.return_value.tables = {'test_table': mock_table}

        # Call function
        delete_table(mock_engine, 'test_table')

        # Assert table drop was called
        mock_table.drop.assert_called_once_with(mock_engine)

    @patch('sqlalchemy.MetaData')
    def test_delete_non_existing_table(self, MockedMetaData):
        # Setup
        mock_engine = MagicMock()
        MockedMetaData.return_value.tables = {}

        # Assert exception is raised for non-existing table
        with self.assertRaises(NoSuchTableError):
            delete_table(mock_engine, 'non_existent_table')

if __name__ == '__main__':
    unittest.main()
