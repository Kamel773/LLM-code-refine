import unittest
from unittest.mock import patch, Mock
import smtplib

class TestEmail(unittest.TestCase):
    @patch("smtplib.SMTP")
    def test_send_email(self, mock_smtp):
        mock_smtp.return_value.starttls.return_value = True
        mock_smtp.return_value.login.return_value = True
        mock_smtp.return_value.sendmail.return_value = True
        mock_smtp.return_value.quit.return_value = True

        result = send_email("smtp.gmail.com", 587, "sender@gmail.com", "password", "receiver@gmail.com", "Test", "This is a test email")

        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()