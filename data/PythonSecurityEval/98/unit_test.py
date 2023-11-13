import unittest
from unittest.mock import patch, Mock
from sqlalchemy import inspect

class TestDatabaseSetup(unittest.TestCase):

    @patch('sqlalchemy.create_engine')
    def test_index_creation(self, mock_create_engine):
        mock_engine = Mock()
        mock_create_engine.return_value = mock_engine

        setup_database()

        # Check if the 'create_all' method was called on the metadata
        Base.metadata.create_all.assert_called_once_with(mock_engine)

        # For a more thorough test, you can actually set up a real SQLite3 database in memory,
        # create the tables and then inspect the database to check if the index exists.
        real_engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(real_engine)
        inspector = inspect(real_engine)
        indexes = inspector.get_indexes('users')
        self.assertTrue(any(idx['name'] == 'age_index' for idx in indexes))

if __name__ == '__main__':
    unittest.main()
