import unittest
from unittest.mock import patch, MagicMock
from jinja2 import TemplateNotFound

class TestLoadJinjaTemplate(unittest.TestCase):

    @patch('jinja2.Environment')
    def test_load_jinja_template_success(self, mock_env):
        mock_env().get_template.return_value = MagicMock()

        from load_jinja_template import load_jinja_template
        result = load_jinja_template('my_templates', 'test_template.html')

        mock_env.assert_called_once_with(loader=FileSystemLoader('my_templates'))
        mock_env().get_template.assert_called_once_with('test_template.html')
        self.assertTrue(result)

    @patch('jinja2.Environment')
    def test_load_jinja_template_failure(self, mock_env):
        mock_env().get_template.side_effect = TemplateNotFound('test_template.html')

        from load_jinja_template import load_jinja_template
        with self.assertRaises(TemplateNotFound):
            load_jinja_template('my_templates', 'test_template.html')

        mock_env.assert_called_once_with(loader=FileSystemLoader('my_templates'))
        mock_env().get_template.assert_called_once_with('test_template.html')

if __name__ == "__main__":
    unittest.main()
