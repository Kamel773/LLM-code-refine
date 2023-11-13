import unittest
from unittest.mock import patch
import your_module  # replace with the name of the module where you defined generate_session_id

class TestGenerateSessionId(unittest.TestCase):
    @patch('your_module.uuid.uuid4')
    def test_generate_session_id(self, mock_uuid):
        mock_uuid.return_value = uuid.UUID('12345678123456781234567812345678')
        result = your_module.generate_session_id()
        self.assertEqual(result, '12345678-1234-5678-1234-567812345678')

if __name__ == '__main__':
    unittest.main()