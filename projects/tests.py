from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from projects.models import Project


class TestProject(TestCase):
    def setUp(self):
        self.user = User(username='test', password='1234')
        self.user.save()
        self.project = Project(name='test_project')
        self.project.save()
        self.project.users.add(self.user.id)

    def test_users(self):
        self.assertEquals(self.project.users.get(username='test'), self.user)