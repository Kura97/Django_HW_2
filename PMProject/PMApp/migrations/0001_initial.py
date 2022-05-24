# Generated by Django 4.0.4 on 2022-05-24 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=' name Project.', max_length=50)),
                ('creation_time', models.DateTimeField(auto_now_add=True, help_text='creation time')),
                ('completion_time', models.DateTimeField(help_text='completion time')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='title the task.', max_length=50)),
                ('description', models.TextField(help_text='the description')),
                ('time_estimate', models.IntegerField(help_text='estimation time')),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
