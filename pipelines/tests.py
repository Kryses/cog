# Create your tests here.
from django.db import IntegrityError
from django.test import TestCase

from cog.base_classes.test_classes import UserProjectBaseClass
from pipelines.models import Status, PipelineTemplate, WorkflowTemplate


class TestPipeline(UserProjectBaseClass):
    def test_status(self):
        self.assertTrue(False)

    def test_percent_conmplete(self):
        self.assertTrue(False)

    def test_upstream_pipelines(self):
        self.assertTrue(False)

    def test_downstream_pipelines(self):
        self.assertTrue(False)

    def test_tasks(self):
        self.assertTrue(False)

    def test_parent_pipeline(self):
        self.assertTrue(False)

    def test_child_pipelines(self):
        self.assertTrue(False)


class TestWorkflow(UserProjectBaseClass):
    def test_status(self):
        self.assertTrue(False)

    def test_percent_conmplete(self):
        self.assertTrue(False)

    def test_upstream_pipelines(self):
        self.assertTrue(False)

    def test_downstream_pipelines(self):
        self.assertTrue(False)

    def test_tasks(self):
        self.assertTrue(False)

    def test_parent_pipeline(self):
        self.assertTrue(False)

    def test_child_pipelines(self):
        self.assertTrue(False)


class TestTask(UserProjectBaseClass):
    def test_assigned_user(self):
        self.assertTrue(False)

    def test_status(self):
        self.assertTrue(False)

    def test_time_logged(self):
        self.assertTrue(False)

    def test_parent_task(self):
        self.assertTrue(False)

    def test_child_tasks(self):
        self.assertTrue(False)


class TestStatus(UserProjectBaseClass):
    def setUp(self):
        super(TestStatus, self).setUp()
        self.status = Status.objects.create(name='waiting', project=self.project)

    def test_name(self):
        """Test quary by name."""

        status = Status.objects.get(name='waiting')
        self.assertEquals(status.name, 'waiting')

    def test_unique(self):
        """Test to make sure the unique constraint is working."""

        status = Status.objects.create(name='ready', project=self.project)
        self.assertIsNotNone(status)

        with self.assertRaises(IntegrityError):
            status = Status.objects.create(name='waiting', project=self.project)



class TestPipelineTemplate(UserProjectBaseClass):

    def setUp(self):
        super(TestPipelineTemplate, self).setUp()
        self.pipeline_template = PipelineTemplate.objects.create(name='Test Pipeline Template', project=self.project)
        self.workflows_names = ['Create Controls', 'Do a thing', 'Do another thing']
        workflows_templates = map(lambda x: WorkflowTemplate(name=x, project=self.project), self.workflows_names)
        WorkflowTemplate.objects.bulk_create(workflows_templates)


    def test_name(self):
        pipeline = PipelineTemplate.objects.get(name='Test Pipeline Template')
        self.assertEquals(pipeline.name, 'Test Pipeline Template')

    def test_workflows(self):
        workflows = WorkflowTemplate.objects.filter(name__in=self.workflows_names)
        self.pipeline_template.workflows.add(*workflows)
        self.assertEquals(list(self.pipeline_template.workflows.values_list('name', flat=True)), self.workflows_names)

    def test_parent_pipeline(self):
        self.assertTrue(False)

    def test_child_pipelines(self):
        self.assertTrue(False)


class TestTaskTemplate(TestCase):
    def setUp(self):
        pass

    def test_name(self):
        self.assertTrue(False)

    def test_status(self):
        self.assertTrue(False)

    def test_parent_task(self):
        self.assertTrue(False)

    def test_child_tasks(self):
        self.assertTrue(False)
