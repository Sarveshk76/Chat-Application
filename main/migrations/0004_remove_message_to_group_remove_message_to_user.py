# Generated by Django 4.0 on 2023-01-09 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_message_to_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='to_group',
        ),
        migrations.RemoveField(
            model_name='message',
            name='to_user',
        ),
    ]
