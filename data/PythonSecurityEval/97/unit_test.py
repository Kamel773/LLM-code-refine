import unittest
from unittest.mock import patch, Mock
import smtplib

class TestEmail(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        mock_smtp.return_value.login.return_value = True
        mock_smtp.return_value.sendmail.return_value = True
        mock_smtp.return_value.quit.return_value = True

        subject = 'Test Subject'
        message = 'Test Message'
        to_email = 'test@example.com'

        send_email(subject, message, to_email)

        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        mock_smtp.return_value.login.assert_called_once_with('your_email@gmail.com', 'your_password')
        mock_smtp.return_value.sendmail.assert_called_once_with('your_email@gmail.com', to_email, ANY)
        mock_smtp.return_value.quit.assert_called_once()

if __name__ == '__main__':
    unittest.main()