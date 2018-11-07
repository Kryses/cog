from django.db import models

# Create your models here.
from cog.base_classes.base_models import BaseModel, UserMixin
from projects.models import ProjectMixin


class NotesMixin(models.Model, UserMixin):
    notes = models.ManyToManyField('notes.Notes', related_name='%(class)s_created_by', null=True)


class Note(BaseModel, ProjectMixin):
    text = models.TextField()


class Comment(BaseModel, UserMixin):
    parent = models.ForeignKey('notes.Comment', on_delete=models.SET_NULL, null=True)
    text = models.TextField()
