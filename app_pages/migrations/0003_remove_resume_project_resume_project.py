# Generated by Django 5.0.6 on 2024-06-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pages', '0002_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='project',
        ),
        migrations.AddField(
            model_name='resume',
            name='project',
            field=models.ManyToManyField(to='app_pages.project'),
        ),
    ]
