import unittest
from unittest.mock import patch, Mock
import smtplib

class TestEmail(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        mock_smtp.return_value.login.return_value = True
        mock_smtp.return_value.sendmail.return_value = True
        mock_smtp.return_value.quit.return_value = True

        subject = "Test Subject"
        body = "Test Body"
        to = "test@example.com"
        sender = "sender@example.com"
        password = "password"

        send_email(subject, body, to, sender, password)

        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        mock_smtp.return_value.login.assert_called_once_with(sender, password)
        mock_smtp.return_value.sendmail.assert_called_once_with(sender, to, anything)
        mock_smtp.return_value.quit.assert_called_once()

if __name__ == '__main__':
    unittest.main()