# Generated by Django 5.0.6 on 2024-05-30 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0022_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='Website',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
