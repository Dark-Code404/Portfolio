# Generated by Django 5.0.6 on 2024-05-27 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0016_remove_resumeabout_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumeabout',
            name='Lamguage',
        ),
        migrations.AddField(
            model_name='resumeabout',
            name='Language',
            field=models.TextField(blank=True),
        ),
    ]
