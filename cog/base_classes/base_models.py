from django.contrib.auth.models import User
from django.db import models


class UserMixin(models.Model):
    """Mixin class to add the user column."""

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True


class BaseModel(models.Model):
    """Base model for all models to ensure date created and modified are always included."""

    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='%(class)s_created_by', null=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='%(class)s_modified_by', null=True)

    class Meta:
        abstract = True

    def __repr__(self):
        return "{}: {}, {}".format(self.__class__, self.id, self.name)