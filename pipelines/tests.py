# Create your tests here.
from django.db import IntegrityError

from cog.base_classes.test_classes import UserProjectBaseClass
from pipelines.models import Pipeline, PipelineTemplate, Status, Task, TaskTemplate, Workflow, WorkflowTemplate


class TestPipeline(UserProjectBaseClass):

    def setUp(self):
        super().setUp()
        self.status = Status.objects.create(name='ready', project=self.project)
        self.pipeline = Pipeline.objects.create(name='Test', project=self.project, status=self.status)

    def test_status(self):
        self.assertEquals(self.pipeline.status.name, 'ready')

    def test_percent_conmplete(self):
        self.assertEquals(self.pipeline.percent_completed, 0.0)

    def test_upstream(self):
        pipeline_names = ['Test 1', 'Test 2']
        pipelines = map(lambda x: Pipeline(name=x, project=self.project), pipeline_names)
        Pipeline.objects.bulk_create(pipelines)
        pipelines = Pipeline.objects.filter(name__in=pipeline_names)
        self.pipeline.upstream.add(*pipelines)
        self.assertEquals(list(self.pipeline.upstream.values_list('name', flat=True)), pipeline_names)

    def test_downstream(self):
        pipeline_names = ['Test 1', 'Test 2']
        pipelines = map(lambda x: Pipeline(name=x, project=self.project), pipeline_names)
        Pipeline.objects.bulk_create(pipelines)
        pipelines = Pipeline.objects.filter(name__in=pipeline_names)
        self.pipeline.downstream.add(*pipelines)
        self.assertEquals(list(self.pipeline.downstream.values_list('name', flat=True)), pipeline_names)

    def test_workflows(self):
        workflow_nams = ['Task 1', 'Task 2']
        workflows = map(lambda x: Workflow(name=x, project=self.project), workflow_nams)
        Workflow.objects.bulk_create(workflows)
        workflow_objects = Workflow.objects.filter(name__in=workflow_nams)
        self.pipeline.workflows.add(*workflow_objects)
        self.assertEquals(list(self.pipeline.workflows.values_list('name', flat=True)), workflow_nams)


class TestWorkflow(UserProjectBaseClass):

    def setUp(self):
        super().setUp()
        self.status = Status.objects.create(name='ready', project=self.project)
        self.workflow = Workflow.objects.create(name='Test Task', project=self.project, status=self.status)

    def test_status(self):
        self.assertEquals(self.workflow.status.name, 'ready')

    def test_percent_conmplete(self):
        self.assertEquals(self.workflow.percent_complete, 0.0)

    def test_upstream(self):
        workflow_names = ['Test 1', 'Test 2']
        workflows = map(lambda x: Workflow(name=x, project=self.project), workflow_names)
        Workflow.objects.bulk_create(workflows)
        workflows = Workflow.objects.filter(name__in=workflow_names)
        self.workflow.upstream.add(*workflows)
        self.assertEquals(list(self.workflow.upstream.values_list('name', flat=True)), workflow_names)

    def test_downstream(self):
        workflow_names = ['Test 1', 'Test 2']
        workflows = map(lambda x: Workflow(name=x, project=self.project), workflow_names)
        Workflow.objects.bulk_create(workflows)
        workflows = Workflow.objects.filter(name__in=workflow_names)
        self.workflow.downstream.add(*workflows)
        self.assertEquals(list(self.workflow.downstream.values_list('name', flat=True)), workflow_names)

    def test_tasks(self):
        task_names = ['Task 1', 'Task 2']
        tasks = map(lambda x: Task(name=x, project=self.project), task_names)
        Task.objects.bulk_create(tasks)
        task_objects = Task.objects.filter(name__in=task_names)
        self.workflow.tasks.add(*task_objects)
        self.assertEquals(list(self.workflow.tasks.values_list('name', flat=True)), task_names)


class TestTask(UserProjectBaseClass):

    def setUp(self):
        super(TestTask, self).setUp()
        self.status = Status.objects.create(name='ready', project=self.project)
        self.task = Task.objects.create(name='Test Task', project=self.project, assigned_user=self.user,
                                        status=self.status)

    def test_assigned_user(self):
        self.assertEquals(self.task.assigned_user, self.user)

    def test_status(self):
        self.assertEquals(self.status.name, 'ready')

    def test_upstream(self):
        task_names = ['Test 1', 'Test 2']
        tasks = map(lambda x: Task(name=x, project=self.project), task_names)
        Task.objects.bulk_create(tasks)
        tasks = Task.objects.filter(name__in=task_names)
        self.task.upstream.add(*tasks)
        self.assertEquals(list(self.task.upstream.values_list('name', flat=True)), task_names)

    def test_downstream(self):
        task_names = ['Test 1', 'Test 2']
        tasks = map(lambda x: Task(name=x, project=self.project), task_names)
        Task.objects.bulk_create(tasks)
        tasks = Task.objects.filter(name__in=task_names)
        self.task.upstream.add(*tasks)
        self.assertEquals(list(self.task.upstream.values_list('name', flat=True)), task_names)


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

    def test_upstream(self):
        pipeline_names = ['Test 1', 'Test 2']
        pipeline_templates = map(lambda x: PipelineTemplate(name=x, project=self.project), pipeline_names)
        PipelineTemplate.objects.bulk_create(pipeline_templates)
        pipeline_templates = PipelineTemplate.objects.filter(name__in=pipeline_names)
        self.pipeline_template.upstream.add(*pipeline_templates)
        self.assertEquals(list(self.pipeline_template.upstream.values_list('name', flat=True)), pipeline_names)

    def test_downstream(self):
        pipeline_names = ['Test 1', 'Test 2']
        pipeline_templates = map(lambda x: PipelineTemplate(name=x, project=self.project), pipeline_names)
        PipelineTemplate.objects.bulk_create(pipeline_templates)
        pipeline_templates = PipelineTemplate.objects.filter(name__in=pipeline_names)
        self.pipeline_template.downstream.add(*pipeline_templates)
        self.assertEquals(list(self.pipeline_template.downstream.values_list('name', flat=True)), pipeline_names)

    def test_unique(self):
        with self.assertRaises(IntegrityError):
            PipelineTemplate.objects.create(name='Test Pipeline Template', project=self.project)


class TestTaskTemplate(UserProjectBaseClass):
    def setUp(self):
        super(TestTaskTemplate, self).setUp()
        self.status = Status.objects.create(name='ready', project=self.project)
        self.task_template = TaskTemplate.objects.create(name='Test')

    def test_name(self):
        task_template = TaskTemplate.objects.get(name='Test')
        self.assertEquals(task_template.name, 'Test')

    def test_status(self):
        self.assertEquals(self.task_template.status.name, 'ready')

    def test_upstream(self):
        template_names = ['Test 1', 'Test 2']
        task_tmeplates = map(lambda x: TaskTemplate(name=x, project=self.project), template_names)
        TaskTemplate.objects.bulk_create(task_tmeplates)
        task_tmeplates = TaskTemplate.objects.filter(name__in=template_names)
        self.task_template.upstream.add(*task_tmeplates)
        self.assertEquals(list(self.task_template.upstream.values_list('name', flat=True)), template_names)

    def test_downstream(self):
        template_names = ['Test 1', 'Test 2']
        task_tmeplates = map(lambda x: TaskTemplate(name=x, project=self.project), template_names)
        TaskTemplate.objects.bulk_create(task_tmeplates)
        task_tmeplates = TaskTemplate.objects.filter(name__in=template_names)
        self.task_template.downstream.add(*task_tmeplates)
        self.assertEquals(list(self.task_template.downstream.values_list('name', flat=True)), template_names)
