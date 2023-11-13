import unittest
from unittest.mock import patch, Mock
import smtplib

class TestSendEmail(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        smtp_instance = Mock()
        mock_smtp.return_value = smtp_instance

        send_email('smtp.gmail.com', 'test@gmail.com', 'password', 'recipient@gmail.com', 'Test', 'This is a test')

        mock_smtp.assert_called_with('smtp.gmail.com')
        smtp_instance.starttls.assert_called_with()
        smtp_instance.login.assert_called_with('test@gmail.com', 'password')
        smtp_instance.sendmail.assert_called_with('test@gmail.com', 'recipient@gmail.com', ANY)
        smtp_instance.quit.assert_called_with()

if __name__ == '__main__':
    unittest.main()