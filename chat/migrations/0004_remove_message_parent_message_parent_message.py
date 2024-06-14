# Generated by Django 5.0.6 on 2024-06-02 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='parent',
        ),
        migrations.AddField(
            model_name='message',
            name='parent_message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='chat.message'),
        ),
    ]
