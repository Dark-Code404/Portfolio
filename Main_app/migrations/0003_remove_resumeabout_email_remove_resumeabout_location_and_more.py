# Generated by Django 4.2.12 on 2024-07-31 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0002_remove_about_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumeabout',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='resumeabout',
            name='Location',
        ),
        migrations.RemoveField(
            model_name='resumeabout',
            name='Phone',
        ),
    ]
