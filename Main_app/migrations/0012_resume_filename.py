# Generated by Django 5.0.6 on 2024-05-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0011_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='fileName',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
