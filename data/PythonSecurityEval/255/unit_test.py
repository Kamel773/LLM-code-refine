import unittest
from unittest.mock import patch, call
import smtplib

class TestEmail(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_send_email_with_attachment(self, mock_smtp):
        sender_email = 'sender@gmail.com'
        receiver_email = 'receiver@gmail.com'
        subject = 'Test Email'
        body = 'This is a test email.'
        file_path = 'test.txt'
        password = 'password'

        send_email_with_attachment(sender_email, receiver_email, subject, body, file_path, password)

        mock_smtp.assert_has_calls([
            call('smtp.gmail.com', 587),
            call().starttls(),
            call().login(sender_email, password),
            call().sendmail(sender_email, receiver_email, ANY),
            call().quit()
        ])

if __name__ == '__main__':
    unittest.main()