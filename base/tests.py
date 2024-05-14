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

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.task1 = Task.objects.create(
            title='Test Task 1',
            description='This is a test task',
            user=self.user1
        )

    def test_task_list_GET(self):
        self.client.login(username='testuser1', password='12345')
        response = self.client.get(reverse('tasks'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task 1')
        self.assertTemplateUsed(response, 'base/task_list.html')

    def test_task_detail_GET(self):
        self.client.login(username='testuser1', password='12345')
        response = self.client.get(reverse('task', args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task 1')
        self.assertTemplateUsed(response, 'base/task.html')

    def test_task_create_POST(self):
        self.client.login(username='testuser1', password='12345')
        response = self.client.post(reverse('task-create'),
            {
                'title': 'Test Task 2',
                'description': 'This is a second test task',
                'user': self.user1.id
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.last().title, 'Test Task 2')

    def test_task_update_POST(self):
        self.client.login(username='testuser1', password='12345')
        response = self.client.post(reverse('task-update', args=[1]),
            {
                'title': 'Updated Task',
                'description': 'This is an updated test task',
                'user': self.user1.id
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.first().title, 'Updated Task')

    def test_task_delete_POST(self):
        self.client.login(username='testuser1', password='12345')
        response = self.client.post(reverse('task-delete', args=[1]))

        self.assertEqual(response.status_code, 302)  # Expecting a redirect after deletion
        self.assertFalse(Task.objects.filter(id=1).exists())
