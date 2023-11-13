import unittest
from unittest.mock import patch, Mock
from your_module import remove_script_tags  # replace 'your_module' with the name of your module

class TestRemoveScriptTags(unittest.TestCase):
    @patch('your_module.re.sub')  # replace 'your_module' with the name of your module
    def test_remove_script_tags(self, mock_sub):
        mock_sub.return_value = 'cleaned content'
        content = '<script>some script</script>'
        result = remove_script_tags(content)
        mock_sub.assert_called_once_with('<script.*?>.*?</script>', '', content, flags=re.DOTALL)
        self.assertEqual(result, 'cleaned content')

if __name__ == '__main__':
    unittest.main()