import unittest
from unittest.mock import patch, Mock
import smtplib

class TestEmail(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        mock_server = Mock()
        mock_smtp.return_value = mock_server

        send_email('test_email@gmail.com', 'test_password')

        mock_smtp.assert_called_with('smtp.gmail.com', 587)
        mock_server.starttls.assert_called_with()
        mock_server.login.assert_called_with("your_email@gmail.com", "your_password")
        mock_server.sendmail.assert_called_with("your_email@gmail.com", 'test_email@gmail.com', 'Subject: Your Credentials\n\nYour email is test_email@gmail.com and your password is test_password')
        mock_server.quit.assert_called_with()

if __name__ == '__main__':
    unittest.main()