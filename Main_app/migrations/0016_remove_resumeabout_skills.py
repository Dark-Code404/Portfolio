# Generated by Django 5.0.6 on 2024-05-27 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0015_resumeabout_resumecerti_resumeeducation_resumesoft_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumeabout',
            name='Skills',
        ),
    ]
