# Generated by Django 2.0.9 on 2018-11-22 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pipeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('percent_completed', models.FloatField(default=0.0)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pipeline_created_by', to=settings.AUTH_USER_MODEL)),
                ('downstream', models.ManyToManyField(related_name='pipeline_downstream', to='pipelines.Pipeline')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pipeline_modified_by', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PipelineTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pipelinetemplate_created_by', to=settings.AUTH_USER_MODEL)),
                ('downstream', models.ManyToManyField(related_name='pipelinetemplate_downstream', to='pipelines.PipelineTemplate')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pipelinetemplate_modified_by', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('short_name', models.CharField(max_length=3)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='status_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='status_modified_by', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('assigned_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_created_by', to=settings.AUTH_USER_MODEL)),
                ('downstream', models.ManyToManyField(related_name='task_downstream', to='pipelines.Task')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_modified_by', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Project')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='pipelines.Status')),
                ('upstream', models.ManyToManyField(related_name='task_upstream', to='pipelines.Task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasktemplate_created_by', to=settings.AUTH_USER_MODEL)),
                ('downstream', models.ManyToManyField(related_name='tasktemplate_downstream', to='pipelines.TaskTemplate')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasktemplate_modified_by', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Project')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='pipelines.Status')),
                ('upstream', models.ManyToManyField(related_name='tasktemplate_upstream', to='pipelines.TaskTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('percent_complete', models.FloatField(default=0.0)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workflow_created_by', to=settings.AUTH_USER_MODEL)),
                ('downstream', models.ManyToManyField(related_name='workflow_downstream', to='pipelines.Workflow')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workflow_modified_by', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Project')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='pipelines.Status')),
                ('tasks', models.ManyToManyField(to='pipelines.Task')),
                ('upstream', models.ManyToManyField(related_name='workflow_upstream', to='pipelines.Workflow')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkflowTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workflowtemplate_created_by', to=settings.AUTH_USER_MODEL)),
                ('downstream', models.ManyToManyField(related_name='workflowtemplate_downstream', to='pipelines.WorkflowTemplate')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workflowtemplate_modified_by', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Project')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='pipelines.Status')),
                ('tasks', models.ManyToManyField(to='pipelines.TaskTemplate')),
                ('upstream', models.ManyToManyField(related_name='workflowtemplate_upstream', to='pipelines.WorkflowTemplate')),
            ],
        ),
        migrations.AddField(
            model_name='pipelinetemplate',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='pipelines.Status'),
        ),
        migrations.AddField(
            model_name='pipelinetemplate',
            name='upstream',
            field=models.ManyToManyField(related_name='pipelinetemplate_upstream', to='pipelines.PipelineTemplate'),
        ),
        migrations.AddField(
            model_name='pipelinetemplate',
            name='workflows',
            field=models.ManyToManyField(to='pipelines.WorkflowTemplate'),
        ),
        migrations.AddField(
            model_name='pipeline',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='pipelines.Status'),
        ),
        migrations.AddField(
            model_name='pipeline',
            name='upstream',
            field=models.ManyToManyField(related_name='pipeline_upstream', to='pipelines.Pipeline'),
        ),
        migrations.AddField(
            model_name='pipeline',
            name='workflows',
            field=models.ManyToManyField(to='pipelines.Workflow'),
        ),
        migrations.AlterUniqueTogether(
            name='workflowtemplate',
            unique_together={('name', 'project')},
        ),
        migrations.AlterUniqueTogether(
            name='tasktemplate',
            unique_together={('name', 'project')},
        ),
        migrations.AlterUniqueTogether(
            name='status',
            unique_together={('name', 'project')},
        ),
        migrations.AlterUniqueTogether(
            name='pipelinetemplate',
            unique_together={('name', 'project')},
        ),
    ]
