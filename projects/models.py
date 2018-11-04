from django.contrib.auth.models import Group, User
from django.db import models

from cog.base_classes.base_models import BaseModel


class Project(BaseModel):
    """Project Model"""

    users = models.ManyToManyField(User, blank=True)
    groups = models.ManyToManyField(Group, blank=True)


class ProjectMixin(models.Model):
    """Mixin class to add the project column."""

    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True