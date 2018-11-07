from django.db import models

# Create your models here.
from cog.base_classes.base_models import BaseModel
from notes.models import NotesMixin
from pipelines.models import StatusMixin
from projects.models import ProjectMixin


class Asset(BaseModel, StatusMixin, ProjectMixin, NotesMixin):
    asset_type = models.ForeignKey('assets.AssetType')



class AssetType(BaseModel, ProjectMixin):
    class Meta:
        unique_together = ('name', 'project')