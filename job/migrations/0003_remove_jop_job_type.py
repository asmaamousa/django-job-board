# Generated by Django 4.1 on 2022-08-19 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_jop_job_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jop',
            name='job_type',
        ),
    ]
