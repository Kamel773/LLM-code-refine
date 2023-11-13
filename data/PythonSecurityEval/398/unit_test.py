import unittest
from django.db import models
from your_module import create_model  # replace with actual module name

class TestCreateModel(unittest.TestCase):
    def test_create_model(self):
        fields = {
            'name': models.CharField(max_length=255),
            'age': models.IntegerField(),
        }
        MyModel = create_model('MyModel', fields, app_label='myapp')

        self.assertTrue(hasattr(MyModel, 'name'))
        self.assertTrue(hasattr(MyModel, 'age'))

if __name__ == '__main__':
    unittest.main()