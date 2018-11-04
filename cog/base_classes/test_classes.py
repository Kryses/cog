from django.contrib.auth.models import User
from django.test import TestCase

from projects.models import Project


class UserProjectBaseClass(TestCase):
    """Sets up a base user and project for tests"""

    def setUp(self):
        self.user = User.objects.create(username='test', password='1234')
        self.project = Project.objects.create(name='test_project')
        self.project.users.add(self.user.id)