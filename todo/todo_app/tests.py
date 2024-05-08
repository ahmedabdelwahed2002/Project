from django.test import TestCase,Client
from django.contrib.auth.models import User
from .models import Task
from django.urls import reverse

class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.task1 = Task.objects.create(
            title='Test Task 1',
            description='This is a test task',
            user=self.user1
        )

    def test_task_creation(self):
        self.assertEqual(f'{self.task1.title}', 'Test Task 1')
        self.assertEqual(f'{self.task1.description}', 'This is a test task')
        self.assertEqual(f'{self.task1.user}', 'testuser1')