# Generated by Django 5.0.6 on 2024-06-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pages', '0009_remove_project_skil_project_skills_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
