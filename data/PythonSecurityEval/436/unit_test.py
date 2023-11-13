import unittest
from unittest.mock import patch, call
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class TestEmail(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        smtp_server = 'smtp.gmail.com'
        port = 587
        sender_email = 'sender@gmail.com'
        sender_password = 'password'
        receiver_email = 'receiver@gmail.com'
        subject = 'Test Email'
        body = 'This is a test email.'

        send_email(smtp_server, port, sender_email, sender_password, receiver_email, subject, body)

        mock_smtp.assert_called_once_with(smtp_server, port)
        instance = mock_smtp.return_value
        instance.starttls.assert_called_once()
        instance.login.assert_called_once_with(sender_email, sender_password)
        instance.send_message.assert_called_once()
        instance.quit.assert_called_once()

if __name__ == '__main__':
    unittest.main()