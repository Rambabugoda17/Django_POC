from django.test import TestCase
from .models import Employee


# Create your tests here.
class CustomModelTest(TestCase):
    def test_user_creation(self):
        user = Employee.objects.create(
            email='example@gmail.com',
            username='John Doe',
            )
        self.assertEqual(user.email, 'example@gmail.com')
        self.assertEqual(user.username, 'John Doe')
