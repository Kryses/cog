from django.contrib.auth.models import Group, User
from django.db import models

from cog.models import BaseModel


class Project(BaseModel):
    """Project Model"""

    name = models.CharField(max_length=200)
    users = models.ManyToManyField(User, blank=True)
    groups = models.ManyToManyField(Group, blank=True)
