from django.db import models

# Create your models here.
from cog.base_classes.base_models import BaseModel, UserMixin
from pipelines.models import StatusMixin
from projects.models import ProjectMixin


class NotesMixin(models.Model):
    """Apply a notes field to any model."""
    notes = models.ManyToManyField('notes.Note', related_name='%(class)s_notes', null=True)

    class Meta:
        abstract = True


class CommentsMixin(models.Model):
    """Apply a notes field to any model."""
    comments = models.ManyToManyField('notes.Comment', related_name='%(class)s_comments', null=True)

    class Meta:
        abstract = True


class Note(BaseModel, ProjectMixin, StatusMixin, UserMixin, CommentsMixin):
    """A note that can be applied to an asset or, shot that can be used to start a discussion."""

    text = models.TextField()


class Comment(BaseModel, UserMixin):
    """A comment that can be create by a user in a discussion."""

    parent = models.ForeignKey('notes.Comment', on_delete=models.SET_NULL, null=True)
    text = models.TextField()
