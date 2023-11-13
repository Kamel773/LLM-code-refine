import unittest
from unittest.mock import patch, call
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import your_module  # replace with the name of the module where you defined the send_email function

class TestEmail(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        smtp_instance = mock_smtp.return_value

        your_module.send_email('smtp.gmail.com', 587, 'sender@gmail.com', 'password', 'receiver@gmail.com', 'Hello', 'This is a test email')

        mock_smtp.assert_called_with('smtp.gmail.com', 587)
        smtp_instance.starttls.assert_called_with()
        smtp_instance.login.assert_called_with('sender@gmail.com', 'password')
        smtp_instance.sendmail.assert_called_with('sender@gmail.com', 'receiver@gmail.com', ANY)
        smtp_instance.quit.assert_called_with()

if __name__ == '__main__':
    unittest.main()