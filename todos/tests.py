from django.test import TestCase
from .models import Todo

# Create your tests here.

class TotoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='First todo', body='A body here')

    def test_title_contenet(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'

        print("-------------"+expected_object_name)
        self.assertEquals(expected_object_name,'First todo')

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEquals(expected_object_name,'A body here')
