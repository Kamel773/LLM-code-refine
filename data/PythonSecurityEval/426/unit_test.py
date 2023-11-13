import unittest
from unittest.mock import patch, Mock
import your_module  # replace with the name of the module where you defined the send_email function

class TestEmail(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        instance = mock_smtp.return_value
        your_module.send_email('test@example.com', 'Test Subject', 'Test Message')

        # Check that the SMTP server was set up correctly
        mock_smtp.assert_called_with('smtp.gmail.com', 587)
        instance.starttls.assert_called_with()
        instance.login.assert_called_with('your-email@gmail.com', 'your-password')

        # Check that the email was sent with the correct parameters
        instance.sendmail.assert_called_with('your-email@gmail.com', 'test@example.com', ANY)

if __name__ == '__main__':
    unittest.main()