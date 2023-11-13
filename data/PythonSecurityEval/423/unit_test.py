import unittest
from unittest.mock import patch, MagicMock
import your_module  # replace with the name of the module where get_all_emails is defined

class TestGetAllEmails(unittest.TestCase):
    @patch('your_module.create_engine')
    @patch('your_module.MetaData')
    @patch('your_module.Table')
    @patch('your_module.sessionmaker')
    def test_get_all_emails(self, mock_sessionmaker, mock_table, mock_metadata, mock_create_engine):
        mock_session = MagicMock()
        mock_sessionmaker.return_value = mock_session
        mock_query = MagicMock()
        mock_session.query.return_value = mock_query
        mock_query.all.return_value = [('test1@example.com',), ('test2@example.com',)]

        emails = your_module.get_all_emails()

        self.assertEqual(emails, ['test1@example.com', 'test2@example.com'])
        mock_create_engine.assert_called_once_with('sqlite:///users.db')
        mock_metadata.assert_called_once()
        mock_table.assert_called_once_with('users', mock_metadata.return_value, autoload_with=mock_create_engine.return_value)
        mock_sessionmaker.assert_called_once_with(bind=mock_create_engine.return_value)
        mock_session.query.assert_called_once_with(mock_table.return_value.c.email)
        mock_query.all.assert_called_once()

if __name__ == '__main__':
    unittest.main()