from django.db import models

# Create your models here.
from cog.base_classes.base_models import BaseModel
from projects.models import ProjectMixin

DEFAULT_STATUS = 1

class StatusMixin(models.Model):
    """Applies and status column to any model."""
    status = models.ForeignKey('pipelines.Status', on_delete=models.SET_DEFAULT, null=False, default=DEFAULT_STATUS)

    class Meta:
        abstract = True


class TemplateModel(BaseModel):
    """Adds methods to push out templates a unique models."""

    template_model = ""

    def push_template(self, link):
        pass

    class Meta:
        abstract = True


class TaskTemplate(TemplateModel, ProjectMixin, StatusMixin):
    """Used to push out tasks based on."""

    template_model = 'pipelines.Task'
    upstream = models.ManyToManyField('pipelines.TaskTemplate', related_name='%(class)s_upstream')
    downstream = models.ManyToManyField('pipelines.TaskTemplate', related_name='%(class)s_downstream')

    class Meta:
        unique_together = ('name', 'project')


class WorkflowTemplate(TemplateModel, ProjectMixin, StatusMixin):
    """Used to push out new workflows based on the template configuration."""

    template_model = 'pipelines.models.Workflow'
    upstream = models.ManyToManyField('pipelines.WorkflowTemplate', related_name='%(class)s_upstream')
    downstream = models.ManyToManyField('pipelines.WorkflowTemplate', related_name='%(class)s_downstream')
    tasks = models.ManyToManyField('pipelines.TaskTemplate')

    class Meta:
        unique_together = ('name', 'project')


class PipelineTemplate(TemplateModel, ProjectMixin, StatusMixin):
    """Used to push out pipelines base on template configuration."""

    template_model = 'pipelines.models.Pipeline'
    upstream = models.ManyToManyField('pipelines.PipelineTemplate', related_name='%(class)s_upstream')
    downstream = models.ManyToManyField('pipelines.PipelineTemplate', related_name='%(class)s_downstream')
    workflows = models.ManyToManyField('pipelines.WorkflowTemplate')

    class Meta:
        unique_together = ('name', 'project')


class Status(BaseModel, ProjectMixin):
    """A status indicator that can be used across multiple models. These will be unique across projects."""

    short_name = models.CharField(max_length=3)

    class Meta:
        unique_together = ('name', 'project')


class Task(BaseModel, ProjectMixin, StatusMixin):
    """An individual task that can be used in a pipeline."""

    assigned_user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    upstream = models.ManyToManyField('pipelines.Task', related_name='%(class)s_upstream')
    downstream = models.ManyToManyField('pipelines.Task', related_name='%(class)s_downstream')


class Workflow(BaseModel, ProjectMixin, StatusMixin):
    """A collection of task used to accomplish a step in the pipeline."""

    percent_complete = models.FloatField(default=0.0)
    upstream = models.ManyToManyField('pipelines.Workflow', related_name='%(class)s_upstream')
    downstream = models.ManyToManyField('pipelines.Workflow', related_name='%(class)s_downstream')
    tasks = models.ManyToManyField('pipelines.Task')


class Pipeline(BaseModel, ProjectMixin, StatusMixin):
    """A collection of workflows to accompshish an overarcing goal."""

    percent_completed = models.FloatField(default=0.0)
    upstream = models.ManyToManyField('pipelines.Pipeline', related_name='%(class)s_upstream')
    downstream = models.ManyToManyField('pipelines.Pipeline', related_name='%(class)s_downstream')
    workflows = models.ManyToManyField('pipelines.Workflow')
