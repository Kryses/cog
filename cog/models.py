from django.contrib.auth.models import User
from django.db import models

class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='created_by', null=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='modified_by', null=True)

    class Meta:
        abstract = True