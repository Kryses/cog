from rest_framework import serializers

from projects.models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'users', 'groups', 'date_created', 'date_modified', 'created_by', 'modified_by')