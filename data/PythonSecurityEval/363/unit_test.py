import unittest
from unittest.mock import patch, Mock
import smtplib

class TestEmail(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        from_addr = 'myemail@gmail.com'
        password = 'mypassword'
        to_addr = 'youremail@gmail.com'
        subject = 'Test'
        message = 'This is a test.'

        instance = mock_smtp.return_value
        send_email(to_addr, subject, message)

        # Check if the SMTP server was called with the right arguments
        mock_smtp.assert_called_with('smtp.gmail.com', 587)

        # Check if the login was called with the right arguments
        instance.login.assert_called_with(from_addr, password)

        # Check if the sendmail was called with the right arguments
        instance.sendmail.assert_called_with(from_addr, to_addr, message)

if __name__ == '__main__':
    unittest.main()